# 📦 Scrap & Co. – Projet Python

## 🎯 Objectif
Créer une application Python complète pour :
- Scraper des données depuis un site e-commerce
- Stocker les données dans un fichier CSV
- Les analyser avec Pandas
- Générer des visualisations avec Matplotlib
- Regrouper les produits par prix grâce au clustering KMeans (Sklearn)

---

## 🗂 Structure du projet

project/
├── analysis/
│ └── stats.py
├── data/
│ ├── books.csv
│ ├── custom_products.csv
│ ├── histogram_price.png
│ ├── boxplot_price.png
│ ├── clustering_price.png
│ ├── cluster_boxplot.png
├── scraper/
│ ├── book.py
│ ├── scraper_books.py
│ ├── scraper_custom.py
│ ├── exporter.py
│ └── init.py
├── scraper_serpapi.py
├── main.py
├── main_books.py
├── main_stats_books.py
└── README.md

markdown
Copy
Edit

---

## 📘 Partie 1 – Analyse des livres (Books to Scrape)

### 🧾 Données
- Source : [https://books.toscrape.com](https://books.toscrape.com)
- Nombre de livres scrapés : **1000**
- Export : `data/books.csv`

### 📊 Statistiques générales
- Prix moyen : **35,07 €**
- Min : **10 €** / Max : **59,99 €**
- Écart-type : **14,45 €**

### ⭐ Répartition des notes
- One ★ : 226 livres  
- Two ★★ : 196  
- Three ★★★ : 203  
- Four ★★★★ : 179  
- Five ★★★★★ : 196

### 📦 Disponibilité
- 100 % des livres sont "In stock"

### 📈 Visualisations
- `histogram_price.png`  
- `boxplot_price.png`  
- `clustering_price.png`  
- `cluster_boxplot.png`

---

## 🪑 Partie 2 – Analyse de produits réels (chaises ergonomiques)

### 🧾 Données
- Scraping via [SerpAPI](https://serpapi.com) sur Google Shopping
- Requête : "chaise ergonomique"
- Export : `data/custom_products.csv`

### 📊 Étapes réalisées
-  Scraping automatisé
-  Nettoyage des prix
-  Analyse statistique avec Pandas
-  Clustering avec KMeans
-  Visualisations générées :
  - Histogramme
  - Boxplot
  - Clustering
  - Boxplot par cluster

---

##  Technologies

- Python 3
- Pandas
- Matplotlib
- Scikit-learn
- SerpAPI
- BeautifulSoup
- Requests

---

##  Lancer les analyses

###  Livres :
```bash
python main_books.py
python main_stats_books.py
Produits réels (chaises) :
bash
Copy
Edit
python scraper_serpapi.py
python main.py
👩‍💻 Réalisé par
Imane Benamar 💖
Master Chef de Projet Data & IA