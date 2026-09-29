from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def collect(url: str) -> str:
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page(); page.goto(url,wait_until="domcontentloaded")
        html=page.content(); browser.close()
    return BeautifulSoup(html,"html.parser").get_text(" ",strip=True)
