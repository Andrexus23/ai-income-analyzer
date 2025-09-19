"""Entry point."""
from income_analyzer.vector_store import VectorStoreManager
from income_analyzer.llm import LLMManager

if __name__ == "__main__":
    vector_store_manager = VectorStoreManager()
    llm_manager = LLMManager()
    
    while True:
        print("\n\n-------------------------------")
        question = input("Ask your question (q to quit): ")
        print("\n\n")
        if question == "q":
            break
        freelancers = vector_store_manager.retriever.invoke(question)
        response = llm_manager.chain.invoke(
            {
                "reviews": freelancers, 
                "question": question,
            }
        )
        print(response.content)
