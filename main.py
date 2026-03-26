from data_loader import load_all_documents, clean_text
from embedding import Embedding
from vector_store import Vector_Store
from retriever import Retriever
from llm_output_generation import LLM_output

def main():
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
    
    

    
    


    
    