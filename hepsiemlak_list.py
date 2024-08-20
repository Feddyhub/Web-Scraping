import requests
from bs4 import BeautifulSoup as bs

# URL ve headers
url = "https://www.hepsiemlak.com/izmir"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

# Sayfayı çekme
page = requests.get(url, headers=headers)
soup = bs(page.content, "lxml")

price_spans = soup.find_all("span", {"class": "list-view-price"})

# Fiyatları listeye ekleme ve yazdırma
prices = []
for i in price_spans:
    price = i.get_text(strip=True)
    prices.append(price)

# Fiyatları yazdırma
for price in prices:
    print(f"FIYAT:{price}")
    if price>8000:
        print("hello")