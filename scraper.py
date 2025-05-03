from playwright.sync_api import sync_playwright

def save_full_page_html(url, output_filename="output.html"):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)  # Waits up to 60 seconds
            page.wait_for_load_state('networkidle')  # Wait until no more network activity
            html_content = page.content()

            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(html_content)

            print(f"HTML content saved to {output_filename}")
            browser.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
save_full_page_html("https://www.javanelec.com/#dtl/26396")
