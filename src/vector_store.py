import os, numpy as np
import chromadb, uuid
from typing import List, Any
from data_loader import load_all_documents
from embedding import Embedding

class Vector_Store:
    def __init__(self, persistent_dir="../data/vector_store"):
        self.collection = None
        self.client=None
        self.persistent_dir=persistent_dir
        self.collection_name="Collection_PDF"
        
    def prep(self):
        os.makedirs(self.persistent_dir, exist_ok=True)
        self.client = chromadb.PersistentClient(path=self.persistent_dir)
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"desc": "Collection for PDF files"}
        )
        print(f"[DEBUG] Collection: {self.collection}")
    def add_documents(self, documents: List[Any], embeddings: np.ndarray):

        if len(documents) != len(embeddings):
            print("Mismatch happened in length of documents and embeddings")
        ids = []
        metadatas = []
        document_text = []
        embedding_list = []

        for i, (doc,embed) in enumerate(zip(documents,embeddings)):
            id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(id)

            metadata = dict(doc.metadata)
            metadata["doc_index"] = i
            metadata["content_length"] = len(doc.page_content)
            metadatas.append(metadata)

            document_text.append(doc.page_content)
            embedding_list.append(embed.tolist())
        
        self.collection.add(
            ids=ids,
            metadatas=metadatas,
            documents=document_text,
            embeddings=embedding_list
        )
'''  
        print(f"[DEBUG] IDs: {ids} \n ")
        print(f"[DEBUG] Metadata: {metadatas} \n ")
        print(f"[DEBUG] Document_text: {document_text} \n ")
        print(f"[DEBUG] Embedding_list: {embedding_list} \n ")

    
if __name__ == "__main__":
    data = load_all_documents("data")
    obj_embed = Embedding()
    chunks = obj_embed.chunk_docs(data)
    embeddings = obj_embed.embedd_chunks(chunks)
    obj_vs = Vector_Store()
    output = obj_vs.add_documents(chunks,embeddings)
'''
