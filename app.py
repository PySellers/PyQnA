import os
from flask import Flask, request, jsonify, render_template
from qa_engine import ask_question
from document_loader import save_and_load
from index_store import index_documents, load_index, get_index_size, get_document_names

UPLOAD_DIR = "/home/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
load_index()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file selected"}), 400

    path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(path)

    text = save_and_load(path)
    index_documents([text], [file.filename])

    return jsonify({
        "message": "File uploaded and indexed",
        "documents": get_document_names()
    })

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    answer = ask_question(question)
    return jsonify({"answer": answer})

@app.route("/debug/index")
def debug():
    return jsonify({
        "documents_indexed": get_index_size(),
        "files": get_document_names()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
