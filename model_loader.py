# model_loader.py

from sklearn.feature_extraction.text import TfidfVectorizer

def load_vectorizer():
    """
    Loads a TF-IDF vectorizer (lightweight, CPU friendly)
    """
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2)
    )
    return vectorizer
