# RAG Pipeline Project

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG) pipeline** that enhances Large Language Model (LLM) responses by retrieving relevant context from a document store.

The system combines:

* Document ingestion
* Text cleaning
* Embedding generation
* Vector storage
* Retrieval
* LLM-based answer generation

---

## ⚙️ Architecture

1. **Data Loader** → Loads documents
2. **Text Cleaner** → Preprocesses text
3. **Embedding Module** → Converts text into vectors
4. **Vector Store** → Stores embeddings
5. **Retriever** → Fetches relevant documents
6. **LLM Module** → Generates final answer

---

## 📂 Project Structure

```
RAG/
│
├── setup.py
├── requirements.txt
├── data
├── application.py
├── src
    ├──data_loader.py
    ├──embedding.py
    ├──vector_store.py
    ├──retriever.py
    ├──llm_output_generation.py
├── templates/
│   └── start.html
└── README.md
```

---

## 🚀 Features

* End-to-end RAG pipeline
* Chat interface using Flask
* Context-aware responses
* Modular architecture
* Easy integration with custom LLMs

---

## 🛠️ Tech Stack

* Python
* Flask
* LLM (custom / OpenAI / local model)
* Vector Database (ChromaDB/FAISS)

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/JaswanthiKeshav/RAG.git
cd RAG
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python application.py
```

### 4. Open in browser

```
http://localhost:8080
```

---

## 🔄 Workflow

1. User enters a query
2. Query is embedded
3. Retriever finds similar documents
4. Context is passed to LLM
5. LLM generates answer
6. Response displayed in UI

---

## 📸 UI

* Chat-based interface
* Displays user query and bot response
* Option to clear chat history

---

## 🧠 Future Improvements

* Add streaming responses
* Improve retrieval accuracy
* Add multiple document formats (PDF, DOCX)
* Use advanced vector databases (Pinecone, Weaviate)
* Authentication & user sessions

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

Name: Jaswanthi C.K

GitHub: https://github.com/JaswanthiKeshav/RAG
