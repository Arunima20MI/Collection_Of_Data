import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = [book.h3.a["title"] for book in soup.find_all("article", class_="product_pod")]
df_scrape = pd.DataFrame({"Book_Title": titles})
df_scrape.to_csv("scraped_data.csv", index=False)
print("scraped_data.csv created")
