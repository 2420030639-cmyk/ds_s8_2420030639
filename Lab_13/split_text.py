from nltk.tokenize import word_tokenize, sent_tokenize
import nltk


def main():
    nltk.download("punkt")
    nltk.download("punkt_tab")

    text = "The movie was amazing. It had exciting action scenes!"
    print("Word Tokenization:")
    print(word_tokenize(text))
    print("\\nSentence Tokenization:")
    print(sent_tokenize(text))


if __name__ == "__main__":
    main()
