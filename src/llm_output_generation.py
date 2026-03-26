from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from data_loader import load_all_documents,clean_text
from embedding import Embedding
from vector_store import Vector_Store
from retriever import Retriever
from langchain.messages import HumanMessage

class LLM_output:
    def __init__(self):
        self.api_key = "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"
        self.model = "llama-3.1-8b-instant"
        self.llm = ChatGroq(
            api_key = self.api_key,
            model = self.model,
            max_tokens= 1024,
            temperature =0.1
        )

    def rag_pipeline(self,query,obj_retriever):
        results = obj_retriever.retrieve(query = query, top_k = 1)
        print(f"[DEBUG] Results: {results}")
        context = "\n\n".join([d['document_text'] for d in results]) if results else ""
        prompt = PromptTemplate(
            input_variables= ['context', 'question'],
            template = """ Your an AI Assitant
            Context:
            {context}
            Question:
            {question}
            Answer:
            Please answer with a detailed solution
            """
        )
        formatted_prompt = prompt.format(context=context, question=query)

        try:
            #message = [HumanMessage(context=formatted_prompt)]
            response = self.llm.invoke(formatted_prompt)
            return response.content
        except Exception as e:
            raise e

    def main(self,query):
        print(query)
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
        obj_llm = LLM_output()
        answer = obj_llm.rag_pipeline(query,obj_retriever)
        return answer