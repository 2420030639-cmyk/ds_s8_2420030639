from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk


def main():
    nltk.download("punkt")
    nltk.download("punkt_tab")

    sentence = "The players are playing and played different games."
    stemmer = PorterStemmer()
    words = word_tokenize(sentence)

    print("Original words:", words)
    print("Stemmed words:", [stemmer.stem(word) for word in words])


if __name__ == "__main__":
    main()
