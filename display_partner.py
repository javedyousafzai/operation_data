import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://data.unhcr.org/en/partners?page={}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_partners = []

for page in range(1, 97):  # 1 to 96
    url = BASE_URL.format(page)
    print(f"Scraping page {page}...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to load page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Each partner card link contains the ID
    partner_links = soup.select("a[href*='/en/partners/']")

    for link in partner_links:
        name = link.get_text(strip=True)
        href = link.get("href")

        # Extract numeric ID from URL
        # Example: /en/partners/1234
        partner_id = href.rstrip("/").split("/")[-1]

        # Avoid empty or navigation links
        if name and partner_id.isdigit():
            all_partners.append({
                "partner_id": partner_id,
                "partner_name": name
            })

    time.sleep(0.5)  # polite delay

# Remove duplicates (important)
df = pd.DataFrame(all_partners).drop_duplicates()
#in the dataframe, there are repeating partner IDs with different names. can you create a separate column for those repeating IDs and list their corresponding names in that column?# Create a new DataFrame to handle repeating names
repeating_names = df[df.duplicated(subset=['partner_name'], keep=False)]
repeating_names_grouped = repeating_names.groupby('partner_name')['partner_id'].apply(list).reset_index()


# Save to CSV
df.to_csv("unhcr_partners_all_pages.csv", index=False, encoding="utf-8")
# in the csv file there are repeating partner names with different ids. can you create a separate column for those repeating names and list their corresponding ids in that column?# Create a new DataFrame to handle repeating names


print("\nDone!")
print("Total unique partners collected:", len(df))
