import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def main():
    X, y = make_blobs(n_samples=100, centers=3, cluster_std=1.5, random_state=42)
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    model.fit(X)
    labels = model.labels_
    centers = model.cluster_centers_

    print("K-Means Clustering")
    print("Cluster labels:", labels)
    print("Cluster centers:\\n", centers)

    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=200)
    plt.title("K-Means Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()


if __name__ == "__main__":
    main()
