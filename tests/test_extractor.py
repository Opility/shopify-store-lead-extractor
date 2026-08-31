import unittest
from src.main import extract_emails, detect_apps

class TestShopifyExtractor(unittest.TestCase):
    def test_extract_emails(self):
        sample = "Contact support at info@example-store.com for inquiries."
        emails = extract_emails(sample)
        self.assertIn("info@example-store.com", emails)

    def test_detect_apps(self):
        sample_html = '<script src="https://static.klaviyo.com/onsite/js/klaviyo.js"></script>'
        apps = detect_apps(sample_html)
        self.assertIn("Klaviyo", apps)

if __name__ == '__main__':
    unittest.main()
