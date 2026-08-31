# ⚡ Shopify Store Lead Extractor ✅ Emails, Catalog Size & Apps

<div align="center">

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-orange?style=for-the-badge&logo=apify)](https://apify.com/opility/shopify-store-lead-extractor-emails-catalog-size-apps)
[![Status](https://img.shields.io/badge/Status-Live%20%26%20Monetized-brightgreen?style=for-the-badge&logo=github)](https://apify.com/opility/shopify-store-lead-extractor-emails-catalog-size-apps)
[![Pricing](https://img.shields.io/badge/Pricing-%242.00%2F1k%20Leads-blueviolet?style=for-the-badge&logo=shopify)](https://apify.com/opility/shopify-store-lead-extractor-emails-catalog-size-apps)
[![Python](https://img.shields.io/badge/Python-v3.11-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-AI_Agent_Enabled-0A66C2?style=for-the-badge&logo=openai)](https://apify.com/opility/shopify-store-lead-extractor-emails-catalog-size-apps/api/mcp)

---

### Extract verified Shopify Store leads with contact emails, catalog sizes, and installed tech apps ⚡

---

</div>

## 🎯 The Challenge

> **"Finding high-intent e-commerce stores using specific apps like Klaviyo or Yotpo was taking hours of manual digging..."**

| Problem | Impact |
|:---|:---|
| 🛍️ **Manual Store Hunting** | 4-5 hours/day wasted manually checking websites |
| 📧 **Missing Founder Emails** | 70% of lead tools only provide generic `@info.com` addresses |
| 🛠️ **Hidden Tech Stack** | No way to know if stores use Klaviyo, Gorgias, or Recharge |
| 💰 **Overpriced Databases** | Legacy databases charge $5,000–$15,000/year upfront |

---

## ✨ The Solution

### Automated E-Commerce Lead Intelligence Engine

🔍 Target Niche In ➔ 🐍 Python Crawlee + Tech Fingerprint ➔ 📊 Verified Leads Out

**What it does:**
- 🛍️ **Shopify Discovery** - Scrapes 4.5M+ active Shopify stores by niche or keyword
- 📦 **Catalog Size Analysis** - Automatically calculates product catalog count (e.g. 50 vs 5,000 products)
- 🛠️ **Tech Stack Fingerprinting** - Detects installed apps (**Klaviyo, Yotpo, Recharge, Gorgias, Loox, Zendesk, Privy**)
- 📧 **Deep Contact Extraction** - Extracts verified founder & support emails (`support@`, `info@`, `founders@`)
- 📱 **Social Media Coordinates** - Scrapes Instagram, TikTok, Facebook, LinkedIn & Twitter/X handles

---

## 📊 Results That Matter

| Metric | Manual Sourcing | Opility Extractor | Impact |
|:---|:---:|:---:|:---:|
| **Sourcing Speed** | 10 stores/hr | **1,000 stores/min** | **+10,000% ⚡** |
| **Email Accuracy** | 30% | **95%+ Verified** | **+65% 🎯** |
| **Tech Stack Detection** | Manual inspection | **100% Automated** | **Instant 🛠️** |
| **Cost Per 1,000 Leads** | $50+ (Virtual Assistant) | **$2.00 Flat** | **-96% ROI 💰** |

---

## 🏆 Key Features

| Feature | Status | Impact |
|:---|:---:|:---|
| 🛍️ **Shopify Store Detection** | ✅ Active | 100% precision filtering |
| 🛠️ **Klaviyo & App Fingerprinting** | ✅ Active | Know their exact tech stack |
| 📦 **Product Catalog Counter** | ✅ Active | Target high-volume stores |
| 📧 **Verified Email Intelligence** | ✅ Active | Reach decision-makers directly |
| 📱 **Social Coordinates Extraction** | ✅ Active | Multi-channel outreach ready |
| 🤖 **MCP & AI Agent API** | ✅ Active | Run via Claude, Cursor, or ChatGPT |

---

## 🛠️ Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/-Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Apify SDK](https://img.shields.io/badge/-Apify_SDK-FF6B35?style=for-the-badge&logo=apify&logoColor=white)
![Crawlee](https://img.shields.io/badge/-Crawlee-0969DA?style=for-the-badge&logo=crawlee&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup4-412991?style=for-the-badge&logo=python&logoColor=white)
![HTTPX](https://img.shields.io/badge/-HTTPX_Async-009688?style=for-the-badge&logo=fastapi&logoColor=white)

</div>

| Tool | Role | Why |
|:---|:---|:---|
| **Apify SDK** | Cloud Serverless Host | Runs proxy rotation, dataset storage & MCP endpoints |
| **Crawlee + HTTPX** | High-Speed Async Engine | Crawls 1,000s of domains concurrently in seconds |
| **BeautifulSoup4** | HTML Parser | Parses meta tags, app scripts, & contact pages |
| **Regex Intelligence** | Pattern Recognition | Extracts clean emails & handles email extension filtering |

---

## 📥 Input Configuration Example

```json
{
  "searchTerms": [
    "Apparel & Fashion",
    "Beauty & Cosmetics",
    "Fitness & Sports",
    "Jewelry & Accessories"
  ],
  "maxResults": 100,
  "detectTechStack": true,
  "proxyConfiguration": {
    "useApifyProxy": true
  }
}
```

---

## 📤 Structured JSON Output Sample

```json
{
  "storeName": "Luxe Apparel Co.",
  "domain": "luxeapparel.com",
  "website": "https://luxeapparel.com",
  "category": "Apparel & Fashion",
  "catalogSize": 342,
  "detectedApps": [
    "Klaviyo",
    "Yotpo",
    "Gorgias",
    "Recharge"
  ],
  "email": "contact@luxeapparel.com",
  "allEmails": [
    "contact@luxeapparel.com",
    "founders@luxeapparel.com"
  ],
  "socialLinks": {
    "instagram": "https://instagram.com/luxeapparel",
    "facebook": "https://facebook.com/luxeapparel",
    "tiktok": "https://tiktok.com/@luxeapparel",
    "linkedin": null
  },
  "source": "Opility Shopify Engine"
}
```

---

## 📁 Repository Structure

```text
shopify-store-lead-extractor/
├── .actor/
│   ├── actor.json
│   ├── input_schema.json
│   └── output_schema.json
├── src/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🏢 Developed & Maintained By

<div align="center">

**Built by Opility** 👨‍💻  
*Empowering Businesses with B2B Lead Automation & Micro-SaaS Engines.*

[![Website](https://img.shields.io/badge/Website-opility.com-0052CC?style=for-the-badge&logo=google-chrome)](https://opility.com)
[![Apify Store](https://img.shields.io/badge/Apify_Store-Opility-FF6B35?style=for-the-badge&logo=apify)](https://apify.com/opility)
[![GitHub](https://img.shields.io/badge/GitHub-Opility-181717?style=for-the-badge&logo=github)](https://github.com/Opility)

</div>

---

<div align="center">

### ⭐ If this project helped you, please star it on GitHub & leave a 5-star review on Apify!
**Made with ❤️ by Opility**

</div>
