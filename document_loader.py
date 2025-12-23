# document_loader.py

import os
from PyPDF2 import PdfReader

def load_documents(upload_folder):
    documents = []

    for file in os.listdir(upload_folder):
        path = os.path.join(upload_folder, file)

        if file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    documents.extend(split_text(text))

        elif file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.extend(split_text(text))

    return documents


def split_text(text, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks
