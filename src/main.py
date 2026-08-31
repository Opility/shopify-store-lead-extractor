import asyncio
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import httpx
from apify import Actor

# App Detection Fingerprints
APP_PATTERNS = {
    'Klaviyo': [r'klaviyo', r'static\.klaviyo\.com'],
    'Yotpo': [r'yotpo', r'staticw2\.yotpo\.com'],
    'Recharge': [r'recharge', r'rechargeassets\.com'],
    'Gorgias': [r'gorgias', r'config\.gorgias\.chat'],
    'Loox': [r'loox\.io', r'loox-images'],
    'Judge.me': [r'judgeme', r'cdn\.judge\.me'],
    'Zendesk': [r'zendesk', r'assets\.zendesk\.com'],
    'Privy': [r'privy\.com', r'widget\.privy\.com'],
    'Smile.io': [r'smile\.io', r'sweettooth'],
}

EMAIL_REGEX = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
IGNORED_EXTS = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'sentry.io', 'wixpress.com'}

def extract_emails(text: str) -> list[str]:
    if not text:
        return []
    matches = EMAIL_REGEX.findall(text)
    cleaned = set()
    for email in matches:
        email = email.lower().strip()
        ext = email.split('.')[-1]
        if ext not in IGNORED_EXTS and not email.endswith(('@example.com', '@domain.com', '@shopify.com')):
            cleaned.add(email)
    return list(cleaned)

def extract_socials(html_text: str) -> dict:
    socials = {'linkedin': None, 'facebook': None, 'instagram': None, 'tiktok': None, 'twitter': None}
    soup = BeautifulSoup(html_text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        try:
            parsed = urlparse(href)
            host = parsed.netloc.lower()
            if 'instagram.com' in host:
                socials['instagram'] = href
            elif 'facebook.com' in host:
                socials['facebook'] = href
            elif 'tiktok.com' in host:
                socials['tiktok'] = href
            elif 'linkedin.com' in host:
                socials['linkedin'] = href
            elif 'twitter.com' in host or 'x.com' in host:
                socials['twitter'] = href
        except Exception:
            pass
    return socials

def detect_apps(html_text: str) -> list[str]:
    detected = []
    for app_name, patterns in APP_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, html_text, re.IGNORECASE):
                detected.append(app_name)
                break
    return detected

async def check_shopify_products_catalog(client: httpx.AsyncClient, domain: str) -> int:
    try:
        url = f"https://{domain}/products.json?limit=250"
        resp = await client.get(url, timeout=7.0, follow_redirects=True)
        if resp.status_code == 200 and 'products' in resp.json():
            products = resp.json()['products']
            return len(products)
    except Exception:
        pass
    return 0

async def main():
    async with Actor:
        actor_input = await Actor.get_input() or {}
        search_terms = actor_input.get('searchTerms', ['Apparel & Fashion', 'Beauty & Cosmetics'])
        max_results = actor_input.get('maxResults', 100)
        detect_tech = actor_input.get('detectTechStack', True)

        Actor.log.info("🚀 Starting Opility Shopify Store Lead Extractor")
        Actor.log.info(f"🔍 Niches: {', '.join(search_terms)} | Max Target: {max_results}")

        total_scraped = 0
        seen_domains = set()

        async with httpx.AsyncClient(headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}) as client:
            for term in search_terms:
                if total_scraped >= max_results:
                    break

                query_url = f"https://html.duckduckgo.com/html/?q={term}+myshopify.com+store"
                try:
                    resp = await client.get(query_url, timeout=10.0)
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    results = soup.find_all('div', class_='result')

                    for res in results:
                        if total_scraped >= max_results:
                            break

                        title_elem = res.find('a', class_='result__url') or res.find('a', class_='result__title')
                        if not title_elem:
                            continue

                        raw_link = title_elem.get('href', '')
                        domain = urlparse(raw_link).netloc.replace('www.', '')

                        if not domain or domain in seen_domains or 'duckduckgo.com' in domain:
                            continue
                        seen_domains.add(domain)

                        store_url = f"https://{domain}"
                        try:
                            site_resp = await client.get(store_url, timeout=10.0, follow_redirects=True)
                            html = site_resp.text
                        except Exception:
                            continue

                        emails = extract_emails(html)
                        socials = extract_socials(html)
                        apps = detect_apps(html) if detect_tech else []
                        catalog_count = await check_shopify_products_catalog(client, domain)

                        lead_record = {
                            "storeName": res.find('a', class_='result__title').text.strip() if res.find('a', class_='result__title') else domain,
                            "domain": domain,
                            "website": store_url,
                            "category": term,
                            "catalogSize": catalog_count,
                            "detectedApps": apps,
                            "email": emails[0] if emails else None,
                            "allEmails": emails,
                            "socialLinks": socials,
                            "source": "Opility Shopify Engine"
                        }

                        await Actor.push_data(lead_record)
                        total_scraped += 1
                        Actor.log.info(f"✅ [{total_scraped}/{max_results}] Found Shopify Store: {domain} | Email: {lead_record['email'] or 'N/A'} | Apps: {', '.join(apps)}")

                except Exception as e:
                    Actor.log.warning(f"Error querying term {term}: {e}")

        Actor.log.info(f"🎉 Scraping finished! Total Shopify Stores Extracted: {total_scraped}")

if __name__ == '__main__':
    asyncio.run(main())
