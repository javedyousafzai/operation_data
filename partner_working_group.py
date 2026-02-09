import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "https://data.unhcr.org/en/partners/view/{}"
output_csv = "unhcr_office_content.csv"

# Headers to appear like a real browser (optional, but helpful)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

with open(output_csv, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["partner_id", "office_content"])

    for partner_id in range(1, 965):
        url = base_url.format(partner_id)
        print(f"Fetching {url} ...")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"  → Skipped (status {response.status_code})")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract all text containing the word "office" (case-insensitive)
            matches = []

            # Search all tags with text
            for tag in soup.find_all(text=True):
                text = tag.strip()
                if "office" in text.lower():
                    # Clean and include
                    clean_text = " ".join(text.split())
                    if clean_text not in matches:
                        matches.append(clean_text)

            # Combine matches into one field
            office_text = " | ".join(matches)

            if office_text:
                writer.writerow([partner_id, office_text])
                print(f"  → Found office text, saved.")
            else:
                print(f"  → No office text found.")

        except Exception as e:
            print(f"  → Error: {e}")

        # Be polite; short delay
        time.sleep(0.5)

print("Done! Saved as", output_csv)
