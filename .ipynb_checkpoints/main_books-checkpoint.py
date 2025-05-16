from scraper.scraper_books import scrape_all
from scraper.exporter import export_books_to_csv

if __name__ == "__main__":
    books = scrape_all(pages=50)
    print(f"✅ Nombre de livres récupérés : {len(books)}")
    export_books_to_csv(books, "data/books.csv")
    print("📁 Fichier 'books.csv' généré avec succès dans /data")
