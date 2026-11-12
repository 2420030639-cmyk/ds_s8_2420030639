import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main():
    movies = pd.DataFrame({
        "Movie": ["Avengers", "Batman", "Superman", "Titanic", "Inception"],
        "Description": [
            "action superhero marvel fight",
            "dark superhero action detective",
            "superhero flying action hero",
            "romance ship love drama",
            "dream science fiction thriller"
        ]
    })

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(movies["Description"])
    similarity = cosine_similarity(matrix)

    movie_name = "Batman"
    movie_index = movies.index[movies["Movie"] == movie_name][0]
    scores = list(enumerate(similarity[movie_index]))
    scores = sorted(scores, key=lambda item: item[1], reverse=True)

    print("Content-Based Recommendations for", movie_name)
    for index, score in scores[1:4]:
        print(movies.iloc[index]["Movie"], "- Similarity:", round(score, 3))


if __name__ == "__main__":
    main()
