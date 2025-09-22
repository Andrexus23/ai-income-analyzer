"""Entry point."""
from income_analyzer.vector_store import VectorStoreManager
from income_analyzer.llm import LLMManager, PromptDebugHandler

if __name__ == "__main__":
    vector_store_manager = VectorStoreManager()
    llm_manager = LLMManager()
    
    while True:
        print("\n\n-------------------------------")
        question = input("Ask your question (q to quit): ")
        print("\n\n")
        if question == "q":
            break
        relevant_items = vector_store_manager.retriever.invoke(question)
        response = llm_manager.chain.invoke(
            {
                "relevant_items": relevant_items, 
                "question": question,
            },
            config={"callbacks": [PromptDebugHandler()]}
        )
        print(response.content)
