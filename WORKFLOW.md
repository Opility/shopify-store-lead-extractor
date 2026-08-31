# 🔄 Workflow Architecture

## Data Flow Diagram
Input Keywords ➔ Niche Search ➔ Store Domain Discovery ➔ Product Catalog Count ➔ App Fingerprint Scan ➔ Email & Social Extraction ➔ Dataset Export

```text
[Input Niche] ---> [DDG Search] ---> [Domain Extractor]
                                           |
                                           v
[Dataset Push] <--- [Email & Socials] <--- [App & Catalog Checker]
```
