from serpapi import GoogleSearch
import csv, os
from pprint import pprint

API_KEY = "9d420701d7e1971f953fbb74dd33b619afa7dece457e2f8bacfb0368fbd64dae"

params = {
    "engine": "google_shopping",
    "q": "chaise ergonomique",
    "hl": "fr",
    "gl": "fr",
    "api_key": API_KEY
}

search = GoogleSearch(params)
results = search.get_dict()


products = results.get("shopping_results", [])

os.makedirs("data", exist_ok=True)

with open("data/custom_products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "source"])
    writer.writeheader()
    for product in products:
        title = product.get("title")
        price = product.get("price")
        source = product.get("source")
        if title and price:
            writer.writerow({
                "title": title,
                "price": price.replace("€", "").replace(",", "."),
                "source": source
            })

print("✅ Produits enregistrés dans data/custom_products.csv")
