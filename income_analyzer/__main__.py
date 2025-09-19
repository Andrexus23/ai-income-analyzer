"""Entry point."""
from income_analyzer.vector_store import VectorStoreManager
from income_analyzer.llm import LLMManager

if __name__ == "__main__":
    vector_store_manager = VectorStoreManager()
    llm_manager = LLMManager()
    print(vector_store_manager.embeddings)
