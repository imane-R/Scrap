import requests
from bs4 import BeautifulSoup
from .book import Book

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    articles = soup.select("article.product_pod")
    for article in articles:
        title = article.h3.a["title"]
        availability = article.select_one(".availability").text.strip()
        rating = article.select_one("p.star-rating")["class"][1]  # ex: "Three"
        price_raw = article.select_one(".price_color").text
        price_clean = (
            price_raw.encode("ascii", "ignore").decode()  # Enlève les caractères foireux
            .replace("£", "")
            .replace("Â", "")  # Si jamais un Â persiste
            .strip()
        )
        
        book = Book(title, float(price_clean), availability, rating)
        books.append(book)

    return books

def scrape_all(pages=50):
    all_books = []
    for i in range(1, pages + 1):
        books = scrape_page(i)
        if books is None:
            break
        all_books.extend(books)
    return all_books
