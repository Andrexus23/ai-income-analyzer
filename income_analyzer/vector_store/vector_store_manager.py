"""Vectore store for passing to llm the most relevant part of dataset."""
import os
from langchain_chroma import Chroma
from langchain_community.embeddings import FastEmbedEmbeddings

from income_analyzer.config import get_config

class VectorStoreManager:
    def __init__(self):
        self.embeddings: FastEmbedEmbeddings = FastEmbedEmbeddings(
            
        )
        self.vector_store = self._initialize_vector_store()
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={'k': config.K_RETRIEVAL}
        )
        
    def _initialize_vector_store(self) -> Chroma:
        """Initialize vector store."""
        add_documents = not os.path.exists(config.DB_LOCATION)