import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize


def main():
    nltk.download("punkt")
    nltk.download("punkt_tab")
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    nltk.download("averaged_perceptron_tagger_eng")

    def wordnet_pos(tag):
        if tag.startswith("J"):
            return wordnet.ADJ
        if tag.startswith("V"):
            return wordnet.VERB
        if tag.startswith("N"):
            return wordnet.NOUN
        if tag.startswith("R"):
            return wordnet.ADV
        return wordnet.NOUN

    sentence = "The students are studying and the cars were moving quickly."
    tokens = word_tokenize(sentence)
    tagged_words = pos_tag(tokens)
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, wordnet_pos(tag)) for word, tag in tagged_words]

    print("Original words:", tokens)
    print("Lemmatized words:", lemmas)


if __name__ == "__main__":
    main()
