from langchain_community.document_loaders import TextLoader,PyMuPDFLoader,PyPDFLoader
from typing import List, Any
from pathlib import Path
import re
def load_all_documents(data_dir: str) -> List[Any]:
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []
    #Text files
    txt_files = list(data_path.glob("**/*.txt"))

    for txt_file in txt_files:
        loader = TextLoader(str(txt_file))
        loaded = loader.load()
        documents.extend(loaded)
        print(f"[DEBUG] Loaded {txt_file}")
    
    #PDF files
    pdf_files = list(data_path.glob("**/*.pdf"))

    for pdf_file in pdf_files:
        loader = PyPDFLoader(str(pdf_file))
        loaded = loader.load()
        documents.extend(loaded)
        print(f"[DEBUG] Loaded {pdf_file}")
    return documents
def clean_text(text):
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'(\d)([A-Za-z])', r'\1 \2', text)
    text = re.sub(r'([A-Za-z])(\d)', r'\1 \2', text)
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)  # handle CAPS joins
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


'''
if __name__ == "__main__":
    docs = load_all_documents("data")
    cleaned_data =[
        {
        "text": clean_text(d.page_content),
        "metadata": d.metadata
        }
        for d in docs
    ]
    print("1. ",cleaned_data[0],"\n2. ", cleaned_data[1],"\n3. ", cleaned_data[2])
    #print(f"Loaded {docs.__len__} documents")

'''




