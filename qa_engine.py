# qa_engine.py

from sklearn.metrics.pairwise import cosine_similarity

class QAEngine:
    def __init__(self, vectorizer):
        self.vectorizer = vectorizer
        self.documents = []
        self.doc_vectors = None

    def index_documents(self, documents):
        """
        Index uploaded document chunks
        """
        self.documents = documents
        self.doc_vectors = self.vectorizer.fit_transform(documents)

    def ask(self, question):
        """
        Find best matching document chunk
        """
        if self.doc_vectors is None:
            return "No documents indexed."

        q_vector = self.vectorizer.transform([question])
        scores = cosine_similarity(q_vector, self.doc_vectors)[0]
        best_idx = scores.argmax()

        return self.documents[best_idx]
