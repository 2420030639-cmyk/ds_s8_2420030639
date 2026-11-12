import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def main():
    ratings = pd.DataFrame({
        "Movie A": [5, 4, 0, 0],
        "Movie B": [4, 5, 0, 0],
        "Movie C": [0, 0, 5, 4],
        "Movie D": [0, 0, 4, 5]
    }, index=["User 1", "User 2", "User 3", "User 4"])

    user_similarity = cosine_similarity(ratings)
    similarity_table = pd.DataFrame(user_similarity, index=ratings.index, columns=ratings.index)

    print("User-Item Ratings:")
    print(ratings)
    print("\\nUser-Based Similarity:")
    print(similarity_table.round(2))

    target_user = "User 1"
    similar_users = similarity_table[target_user].drop(target_user).sort_values(ascending=False)
    print("\\nUsers most similar to", target_user)
    print(similar_users)


if __name__ == "__main__":
    main()
