from transformers import pipeline
from model_loader import model, tokenizer

qa_pipeline = pipeline(
    task="text2text-generation",   # ✅ IMPORTANT
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200
)

def ask_question(context, question):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    result = qa_pipeline(prompt)
    return result[0]["generated_text"]
