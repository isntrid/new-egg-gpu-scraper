import requests
from bs4 import BeautifulSoup

url = "https://www.newegg.com/global/uk-en/p/pl?N=101582760&PageSize=96"
headers = {"User-Agent": "my-scraper/0.1"}
resp = requests.get(url, headers=headers)
html = resp.text

soup = BeautifulSoup(html, "html.parser")

strong_tags = soup.find_all("strong")

model_links = {}

for tag in strong_tags:
    text = tag.get_text(strip=True)
    if text.isdigit() and 100 <= int(text) <= 999:
        container = tag.find_parent("div", class_="item-cell")
        if container:
            link_tag = container.find("a", class_="item-title")
            if link_tag and "href" in link_tag.attrs:
                model_links[int(text)] = link_tag["href"]

if model_links:
    min_model = min(model_links.keys())
    print("Cheapest price: £",min_model)
    print("Link:", model_links[min_model])