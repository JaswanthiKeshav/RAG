import numpy as np
import langchain
from typing import List,Any
from data_loader import load_all_documents
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
class Embedding:
    def __init__(self, chunk_size=1000, chunk_overlap=200, model="all-MiniLM-L6-v2"):
        self.chunk_size = chunk_size
        self.chunk_overlap=chunk_overlap
        self.model=SentenceTransformer(model)

    def chunk_docs(self, documents: List[Any]) -> List[Any]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n","\n"," ",""]
        )
        chunks = splitter.split_documents(documents)
        #print(f"[DEBUG] Chunks {chunks}")
        return chunks
    
    def embedd_chunks(self, chunks:List[Any]) -> np.ndarray:
        text = [chunk.page_content for chunk in chunks]
        chunk_embeddings = self.model.encode(text, show_progress_bar=True)
        #print(f"[DEBUG] embeddings {embeddings}")
        return chunk_embeddings
    def embedd_query(self, query:str):
        query_embedding = self.model.encode(query,show_progress_bar=True)
        return query_embedding

'''  
if __name__ == "__main__":
    docs = load_all_documents("data")
    obj_embedding = Embedding()
    chunks = obj_embedding.chunk_docs(docs)
    embeddings = obj_embedding.embedding(chunks)
    print(embeddings[0])

'''