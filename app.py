# app.py

from flask import Flask, render_template, request
import os

from model_loader import load_vectorizer
from qa_engine import QAEngine
from document_loader import load_documents

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize components
vectorizer = load_vectorizer()
qa_engine = QAEngine(vectorizer)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename:
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
                docs = load_documents(app.config["UPLOAD_FOLDER"])
                qa_engine.index_documents(docs)

        question = request.form.get("question")
        if question:
            answer = qa_engine.ask(question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
