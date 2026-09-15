import time
import os
import fitz
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from playwright.sync_api import sync_playwright

def export_pdf():
    PORT = 8766
    server = HTTPServer(('127.0.0.1', PORT), SimpleHTTPRequestHandler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    print(f"Local server started at port {PORT}")

    output_pdf = os.path.abspath("presentasi_imatika_pkkmb_2026.pdf")
    url = f"http://127.0.0.1:{PORT}/index.html?print-pdf"

    try:
        with sync_playwright() as p:
            # Launch using installed chrome if available or bundled chromium
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_path):
                browser = p.chromium.launch(executable_path=chrome_path, headless=True)
            else:
                browser = p.chromium.launch(headless=True)
            
            page = browser.new_page(viewport={"width": 1920, "height": 1080})
            print(f"Navigating to {url}...")
            page.goto(url, wait_until="networkidle")
            
            # Wait for reveal.js to finish print layout (generates .pdf-page elements)
            page.wait_for_selector(".reveal .slides .pdf-page", timeout=15000)
            print("Reveal.js print view initialized successfully!")
            
            # Small buffer to ensure fonts and syntax highlight are fully painted
            time.sleep(2)
            
            page.pdf(
                path=output_pdf,
                print_background=True,
                prefer_css_page_size=True,
                margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"}
            )
            browser.close()
            print(f"PDF exported to: {output_pdf}")
    finally:
        server.shutdown()

    if os.path.exists(output_pdf):
        size = os.path.getsize(output_pdf)
        doc = fitz.open(output_pdf)
        print(f"VERIFIED: PDF generated successfully with {len(doc)} pages ({size} bytes).")
        for i, page in enumerate(doc):
            first_line = page.get_text("text").strip().split("\n")[0] if page.get_text("text").strip() else "(Visual Slide)"
            print(f"  - Slide {i+1}: {first_line}")
    else:
        raise RuntimeError("PDF export failed: file not created")

if __name__ == "__main__":
    export_pdf()
