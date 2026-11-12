from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


def main():
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("stopwords")

    text = "The movie was amazing and full of exciting action scenes."
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered = [word for word in words if word.isalpha() and word not in stop_words]

    print("Original text:", text)
    print("After stop-word removal:", filtered)


if __name__ == "__main__":
    main()
