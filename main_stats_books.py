from analysis.stats import (
    load_products,
    describe_prices,
    plot_price_histogram,
    plot_price_boxplot,
    price_clustering,
    plot_clusters,
    plot_cluster_boxplot
)

import pandas as pd
import matplotlib.pyplot as plt

df = load_products("data/books.csv")

# Bonus analyse livre : disponibilité
print(" Disponibilité :")
print(df["availability"].value_counts())

# Bonus analyse livre : notation
print(" Répartition des étoiles :")
print(df["rating"].value_counts())

#  Analyse de prix
describe_prices(df)
plot_price_histogram(df)
plot_price_boxplot(df)

# Clustering
df = price_clustering(df)
plot_clusters(df)
plot_cluster_boxplot(df)

print("Analyse des livres terminée")
