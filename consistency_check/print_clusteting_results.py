def print_clusteting_results(articles):
  # 2. Generate SBERT Embeddings
  embeddings = model.encode(news_articles, convert_to_numpy=True)

  # 3. Apply BERTopic
  bertopic_model = BERTopic()
  topics, _ = bertopic_model.fit_transform(news_articles)

  # 4. K-Means Clustering
  num_clusters = 3
  kmeans = KMeans(n_clusters=num_clusters, random_state=42)
  kmeans_labels = kmeans.fit_predict(embeddings)

  # 5. Visualizing Clusters using PCA
  pca = PCA(n_components=2)
  reduced_embeddings = pca.fit_transform(embeddings)

  print(bertopic_model.get_topic_info())
  print("\n### K-Means Clustering ###")
  for i, label in enumerate(kmeans_labels):
      print(f"Article {i}: Cluster {label}")

  plt.figure(figsize=(10, 5))
  sns.scatterplot(x=reduced_embeddings[:, 0], y=reduced_embeddings[:, 1], hue=kmeans_labels, palette="viridis")
  plt.title("K-Means Clustering of News Articles")
  plt.show()
