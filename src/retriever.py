from data_loader import load_all_documents,clean_text
from embedding import Embedding
from vector_store import Vector_Store
import numpy as np

class Retriever:
    def __init__(self,vector_store: Vector_Store, embedding: Embedding):
        self.vectorstore = vector_store
        self.embedding = embedding
    
    def retrieve(self, query: str, top_k: int, score_threshold: float = 0.0):

        
        query_embedding = self.embedding.embedd_query(query)
        #print(f"[DEBUG] Query Embeddings: {query_embedding}")
        print(f"[DEBUG] Collection count: {self.vectorstore.collection.count()}")
        results = self.vectorstore.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=top_k
        )
        
        if results['documents'] and  results['documents'][0]:
            ids = results['ids'][0]
            metadatas = results['metadatas'][0]
            documents = results['documents'][0]
            distances = results['distances'][0]

        retrieved_docs = []
        for i, (id,metadata,doc_text,dist) in enumerate(zip(ids,metadatas,documents,distances)):
            similarity_score = 1 - dist
            print(f"Similarity score: {similarity_score}")

            #if similarity_score >= score_threshold:
            retrieved_docs.append({
                    "ids": id,
                    "metadatas": metadata,
                    "document_text": doc_text,
                    "distance": dist
                })
        #print(f"[DEBUG] Retrieved_docs: {retrieved_docs}")
        return retrieved_docs
        
'''
if __name__ == "__main__":
    data = load_all_documents("data")
    
    for d in data:
        d.page_content = clean_text(d.page_content)
    
    print("After",data[0])
    obj_embed = Embedding()
    
    chunks = obj_embed.chunk_docs(data)
    
    data_embeddings = obj_embed.embedd_chunks(chunks)
    obj_vs = Vector_Store()
    obj_vs.prep()
    
    obj_vs.add_documents(chunks,data_embeddings)
    obj_retriever = Retriever(obj_vs,obj_embed)
    
    output = obj_retriever.retrieve("What is Data Science?",3)
    print(output)
'''