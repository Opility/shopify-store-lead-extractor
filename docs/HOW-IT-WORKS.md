# 📖 How It Works

## 1. Domain Discovery
The engine queries e-commerce directories and search endpoints using target niche parameters.

## 2. Catalog Counter
Sends an async HTTP GET request to `https://{domain}/products.json?limit=250` to inspect catalogue size.

## 3. App Fingerprinting
Inspects raw HTML script tags against regex patterns for Klaviyo, Yotpo, Gorgias, Recharge, Loox, and Zendesk.
