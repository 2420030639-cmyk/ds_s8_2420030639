import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import make_blobs


def main():
    X, y = make_blobs(n_samples=100, centers=3, cluster_std=1.5, random_state=42)
    linked = linkage(X, method="ward")

    print("Hierarchical Clustering")
    print("Linkage matrix:\\n", linked)

    plt.figure(figsize=(10, 5))
    dendrogram(linked)
    plt.title("Hierarchical Clustering Dendrogram")
    plt.xlabel("Data Points")
    plt.ylabel("Distance")
    plt.show()


if __name__ == "__main__":
    main()
