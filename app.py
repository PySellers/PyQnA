import os
from flask import Flask, render_template, request
from document_loader import load_document
from qa_engine import ask_question

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "sample_docs")
os.makedirs(UPLOAD_DIR, exist_ok=True)

DOC_PATH = os.path.join(UPLOAD_DIR, "uploaded.txt")

context_text = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global context_text
    answer = ""

    if request.method == "POST":

        # 1️⃣ Document upload
        if "document" in request.files:
            file = request.files["document"]
            if file.filename != "":
                file.save(DOC_PATH)
                context_text = load_document(DOC_PATH)

        # 2️⃣ Question
        question = request.form.get("question")
        if question and context_text:
            answer = ask_question(context_text, question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
