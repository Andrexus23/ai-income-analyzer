"""Entry point."""
from income_analyzer.vector_store import VectorStoreManager

if __name__ == "__main__":
    vector_store_manager = VectorStoreManager()
    print(vector_store_manager.embeddings)
