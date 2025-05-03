from flask import Flask, send_file
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)

@app.route('/')
def home():
    return 'Scraper is running. Use /scrape to fetch HTML content.'

@app.route('/scrape')
def scrape():
    asyncio.run(run_scraper())
    return send_file('output.html', mimetype='text/html')

async def run_scraper():
    url = 'https://www.javanelec.com/#dtl/36592'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url, wait_until='networkidle')
        await page.wait_for_timeout(3000)  # wait for JS to load
        content = await page.content()
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write(content)
        await browser.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
