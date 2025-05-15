#  Scrap & Co. – Projet Python

##  Objectif
Créer une application Python complète pour :
- Scraper des données depuis un site e-commerce
- Stocker les données dans un fichier CSV
- Les analyser avec Pandas
- Générer des visualisations avec Matplotlib
- Regrouper les produits par prix grâce au clustering KMeans (Sklearn)

---

##  Structure du projet

project/
├── analysis/
│ └── stats.py
├── data/
│ └── custom_products.csv
│ └── histogram_price.png
│ └── boxplot_price.png
│ └── clustering_price.png
│ └── cluster_boxplot.png
├── scraper_serpapi.py
├── main.py
└── README.md


##  Étapes réalisées

✅ Scraping via [SerpAPI](https://serpapi.com) sur Google Shopping pour les **chaises ergonomiques**  
✅ Enregistrement dans `custom_products.csv`  
✅ Analyse statistique avec `pandas`  
✅ Graphiques générés :
- Histogramme
- Boxplot global
- Clustering des prix
- Boxplot par cluster

✅ Clustering automatique avec `KMeans` (3 groupes de prix : bas, moyen, haut)

---

## Technologies

- Python 3
- Pandas
- Matplotlib
- Scikit-learn
- SerpAPI (API de scraping propre)

---

##  Lancer le projet

```bash
# 1. Scraper les produits
python scraper_serpapi.py

# 2. Lancer l'analyse
python main.py
👩‍💻 Réalisé par
Imane Benamar 💖
Master Chef de Projet Data & IA
