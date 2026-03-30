from playwright.sync_api import sync_playwright

def scrape_quotes():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com")

        quotes = page.locator(".quote span.text").all_text_contents()

        browser.close()
        return quotes