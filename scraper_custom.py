import requests
from bs4 import BeautifulSoup
import time
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

def get_html(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
        }

        # Pause entre 1 et 3 secondes
        time.sleep(random.uniform(1, 3))

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    except Exception as e:
        print(f"Erreur lors de la requête : {e}")
        return None

if __name__ == "__main__":
    url = "https://www.cdiscount.com/search/10/chaise+ergonomique.html"
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify()[:1000])  # Affiche les 1000 premiers caractères du HTML