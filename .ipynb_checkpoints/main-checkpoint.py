from analysis.stats import load_products, describe_prices, plot_price_histogram, price_clustering, plot_clusters, plot_cluster_boxplot, plot_price_boxplot, summary_by_cluster

df = load_products("data/custom_products.csv")
describe_prices(df)
plot_price_histogram(df)
plot_price_boxplot(df)
df = price_clustering(df)
plot_clusters(df)
summary_by_cluster(df)
plot_cluster_boxplot(df)

print("✅ Analyse terminée !")
