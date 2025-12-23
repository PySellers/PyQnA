# qa_engine.py
import re
from index_store import get_documents

def polish_answer(text, question):
    sentences = re.split(r'(?<=[.!?])\s+', text)

    question_words = set(re.findall(r"\w+", question.lower()))
    ranked = []

    for s in sentences:
        score = sum(1 for w in question_words if w in s.lower())
        ranked.append((score, s))

    ranked.sort(reverse=True, key=lambda x: x[0])
    best = [s for score, s in ranked if score > 0][:3]

    if not best:
        return "I could not find an exact answer, but the document mentions:\n\n" + text[:300]

    return (
        "Based on your uploaded document, here is the relevant information:\n\n"
        + " ".join(best)
    )

def ask_question(question):
    documents = get_documents()

    if not documents:
        return "No documents indexed. Please upload a document first."

    combined_text = " ".join(documents)
    return polish_answer(combined_text, question)
