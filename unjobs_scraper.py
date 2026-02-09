
import requests
from bs4 import BeautifulSoup
import csv

def scrape_unjobs():
    url = "https://unjobs.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    job_listings = []
    for job_card in soup.find_all("div", class_="job-card"):  # Adjust class based on actual HTML
        title = job_card.find("h3", class_="job-title").text.strip()  # Adjust class
        organization = job_card.find("p", class_="job-organization").text.strip()  # Adjust class
        location = job_card.find("span", class_="job-location").text.strip()  # Adjust class
        link = job_card.find("a", class_="job-link")["href"]  # Adjust class

        job_listings.append({"title": title, "organization": organization, "location": location, "link": link})
    
    return job_listings

def save_to_csv(job_listings, filename="unjobs.csv"):
    keys = job_listings[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(job_listings)

if __name__ == "__main__":
    jobs = scrape_unjobs()
    if jobs:
        save_to_csv(jobs)
        print(f"Scraped {len(jobs)} jobs and saved to unjobs.csv")
    else:
        print("No jobs found or an error occurred.")
