from urllib import response
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import smtplib



URL_AMAZON = 'https://www.amazon.com/dp/B09DYJ5VBV/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B09DYJ5VBV&pd_rd_w=C80uc&content-id=amzn1.sym.e620829b-a408-427e-99ea-7ac734a316f7&pf_rd_p=e620829b-a408-427e-99ea-7ac734a316f7&pf_rd_r=F4XM8Q8ECDHXTB1RSWKW&pd_rd_wg=BHo31&pd_rd_r=2dc1fc1d-449d-440f-86e0-500e54c209b6&s=kitchen&smid=A3D8MT3AQPFLRR&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVjEzSjBNVTE2RjE0JmVuY3J5cHRlZElkPUEwODI2NjE5MlVWNlFJS1VLVEw1NyZlbmNyeXB0ZWRBZElkPUEwOTIwNTgyMTMzUUJGUzc3R0MxMSZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
HEADERS = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept-Language' : 'en-US,en;q=0.5', 
}


response = requests.get(URL_AMAZON, headers = HEADERS )


soup = BeautifulSoup(response.content, "lxml")
price = soup.find_all("span", class_="a-offscreen")[0].text.strip().split("$")[1]






title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 50

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
      
    connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL_AMAZON}"
        )
