import requests
from bs4 import BeautifulSoup as bs
import time

current_price=[]

while True:
    # URL ve headers
    url = "https://www.zara.com/tr/tr/kirisik-efektli-organze-gomlek-p01971154.html?v1=384583608&v2=2419517"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

# Sayfayı çekme
    page = requests.get(url, headers=headers)
    soup = bs(page.content, "lxml")

    price_spans = soup.find_all("span", {"class": "money-amount__main"})

    # Fiyatları listeye ekleme ve yazdırma
    prices = []
    for i in price_spans:
        price = i.get_text(strip=True)
        prices.append(price)
    print(prices)
    # Fiyatları yazdırma
   

# Neden for dongusu ve dizi kullandim ?
# Otomatize etmek trigger eklemek
    
    time.sleep(30)  
    