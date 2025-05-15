import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def load_products(filepath):
    df = pd.read_csv(filepath)
    df["price"] = df["price"].astype(float)  # Nettoyage : prix en float
    return df

def describe_prices(df):
    print(df["price"].describe())

def plot_price_histogram(df):
    plt.hist(df["price"], bins=20)
    plt.title("Histogramme des prix")
    plt.xlabel("Prix (€)")
    plt.ylabel("Nombre de produits")
    plt.savefig("data/histogram_price.png")
    plt.close()

def price_clustering(df, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
    df["price_cluster"] = kmeans.fit_predict(df[["price"]])
    return df

def plot_clusters(df):
    plt.scatter(range(len(df)), df["price"], c=df["price_cluster"])
    plt.title("Clusters de prix")
    plt.xlabel("Produit")
    plt.ylabel("Prix (€)")
    plt.savefig("data/clustering_price.png")
    plt.close()
    
def plot_price_boxplot(df):
    plt.boxplot(df["price"])
    plt.title("Boxplot des prix")
    plt.ylabel("Prix (€)")
    plt.savefig("data/boxplot_price.png")
    plt.close()

def summary_by_cluster(df):
    print("\n📊 Statistiques par cluster :")
    print(df.groupby("price_cluster")["price"].describe())

def plot_cluster_boxplot(df):
    df.boxplot(column="price", by="price_cluster")
    plt.title("Boxplot des prix par cluster")
    plt.suptitle("")  # Supprime le titre par défaut
    plt.xlabel("Cluster")
    plt.ylabel("Prix (€)")
    plt.savefig("data/cluster_boxplot.png")
    plt.close()

