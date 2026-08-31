# 🔌 API & MCP Setup Guide

## Calling via Apify Client API (Python)
```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("opility/shopify-store-lead-extractor-emails-catalog-size-apps").call(
    run_input={"searchTerms": ["Apparel & Fashion"], "maxResults": 50}
)
```

## Model Context Protocol (MCP) Integration
URL: `https://apify.com/opility/shopify-store-lead-extractor-emails-catalog-size-apps/api/mcp`
