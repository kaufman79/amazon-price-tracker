from bs4 import BeautifulSoup
import requests
import send_email

url = "https://www.amazon.com/KitchenAid-KSM150PSWH-Artisan-Pouring-Shield/dp/B00005UP2K/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=NGgII&content-id=amzn1.sym.352fa4e9-2aa8-47c3-b5ac-8a90ddbece20%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=352fa4e9-2aa8-47c3-b5ac-8a90ddbece20&pf_rd_r=MVNP0WTXGH69TVB229TX&pd_rd_wg=NS1gI&pd_rd_r=1d8b0c1f-1bbd-4f23-84b3-9c5cc2c866f1&pd_rd_i=B00005UP2K"

response = requests.get(url,
                        headers={
                            "Accept-Language": "en-US,en;q=0.9,he;q=0.8,el;q=0.7,la;q=0.6",
                            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                            "Accept-Encoding": "gzip, deflate, br, zstd",
                            "Priority": "u=1",
                            "Sec-Fetch-Dest": "document",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-Site": "cross-site",
                            "Sec-Fetch-User": "?1"
                        })
site = response.text
soup = BeautifulSoup(site, "html.parser")

price = float(soup.find(class_="a-price-whole").text + soup.find(class_="a-price-fraction").text)

target_price = 450

if price <= target_price:
    subject = "Your Amazon item is below the designated amount!"
    body = f"Check it out, your item is ${price}!"
    message = f"Subject: {subject}\n\n{body}\n{url}"

    send_email.send_email(message)
