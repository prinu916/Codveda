import requests
from bs4 import BeautifulSoup
import csv
URL = "https://www.bbc.com/news"


response = requests.get(URL)
if response.status_code != 200:
    print("⚠️ Failed to retrieve the web page.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h3")
data = []
for i, headline in enumerate(headlines, 1):
    title = headline.get_text().strip()
    if title:  
        data.append([i, title])

with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["S.No", "Headline"])
    writer.writerows(data)

print("✅ Data scraping completed successfully!")
print(f"🗂️ {len(data)} headlines saved to 'scraped_data.csv'")
