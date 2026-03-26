from flask import Flask,render_template,request, redirect, url_for, session
from llm_output_generation import LLM_output
from data_loader import load_all_documents, clean_text
from embedding import Embedding
from vector_store import Vector_Store
from retriever import Retriever
from main import main
from llm_output_generation import LLM_output

application = Flask(__name__)
app = application
app.secret_key="secret"


@app.route('/', methods=['GET', 'POST'])
def startup():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        query = request.form.get("question")

        obj_llm = LLM_output()
        answer = obj_llm.main(query)

        chat_history = session['chat_history']
        chat_history.append({
            "question": query,
            "answer": answer
        })

        # ✅ Save back to session
        session['chat_history'] = chat_history

        # ✅ Pass chat_history to template
        return render_template('start.html', chat_history=chat_history)

    # GET request
    return render_template('start.html', chat_history=session['chat_history'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)