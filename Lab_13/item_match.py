import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def main():
    ratings = pd.DataFrame({
        "User 1": [5, 4, 0, 0],
        "User 2": [4, 5, 0, 0],
        "User 3": [0, 0, 5, 4],
        "User 4": [0, 0, 4, 5]
    }, index=["Movie A", "Movie B", "Movie C", "Movie D"])

    item_similarity = cosine_similarity(ratings)
    similarity_table = pd.DataFrame(item_similarity, index=ratings.index, columns=ratings.index)

    print("Movie Ratings:")
    print(ratings)
    print("\\nItem-Based Similarity:")
    print(similarity_table.round(2))

    selected_item = "Movie A"
    print("\\nMovies similar to", selected_item)
    print(similarity_table[selected_item].drop(selected_item).sort_values(ascending=False))


if __name__ == "__main__":
    main()
