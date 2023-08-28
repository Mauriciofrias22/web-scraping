import requests
from bs4 import BeautifulSoup
import pandas as pd
books =[]
for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)  # get the response from url
    response = response.content
    soup = BeautifulSoup(response, "html.parser")
    order_list = soup.find("ol")
    articles = order_list.find_all("article", class_="product_pod")
    for article in articles:
        image = article.find("img")
        title = image.attrs["alt"]
        stars = article.find("p")
        stars = stars["class"][1]
        price = article.find("p", class_="price_color").text
        price = float(price[1:])
        books.append([title, stars, price])
        #print(price)
#print(books)
#create the DataFrame
df = pd.DataFrame(books, columns=['title', 'price', 'Star Rating'])
#save as a CSV file
df.to_csv("books.csv")