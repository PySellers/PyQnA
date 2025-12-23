# index_store.py

documents = []
document_names = []

def index_documents(texts, filenames=None):
    global documents, document_names
    documents.extend(texts)
    if filenames:
        document_names.extend(filenames)

def get_documents():
    return documents

def get_index_size():
    return len(documents)

def get_document_names():
    return document_names

def load_index():
    pass  # in-memory index only
