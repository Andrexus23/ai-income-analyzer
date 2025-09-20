"""Vectore store for passing to llm the most relevant part of dataset."""
import os
import pandas as pd
from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.vectorstores.base import VectorStoreRetriever
from langchain_community.embeddings import FastEmbedEmbeddings

from income_analyzer.config import get_config
from income_analyzer.common.constants import K_RELEVANT
from income_analyzer.data_processing import DataProcessor

class VectorStoreManager:
    def __init__(self):
        self.embeddings: FastEmbedEmbeddings = FastEmbedEmbeddings(
            model_name=get_config().vector_store_settings.embeddings_model,
        )
        self.vector_store: Chroma = self._initialize_vector_store()
        self.retriever: VectorStoreRetriever = self.vector_store.as_retriever(
            search_kwargs={
                'k': K_RELEVANT,
            },
        )
        
    def _initialize_vector_store(self) -> Chroma:
        """Initialize vector store."""
        add_documents: bool = not os.path.exists(get_config().vector_store_settings.db_path)
        vector_store: Chroma = Chroma(
            collection_name=get_config().vector_store_settings.db_name,
            persist_directory=get_config().vector_store_settings.db_path,
            embedding_function=self.embeddings,
        )
        if add_documents:
            self._add_initial_documents(vector_store)
            
        return vector_store
        
        
    def _add_initial_documents(self, vector_store: Chroma):
        """Add documents at the first time."""
        df: pd.DataFrame =  pd.read_csv(get_config().data_settings.dataset_path)
        data_processor: DataProcessor = DataProcessor(df)
        statistics = data_processor.aggregate_statistics_for_documents()
        documents: List = []
        ids: List = []

        for i, row in df.iterrows():
            document = Document(
                page_content=row['Title'] + ' ' + row['Review'],
                metadata={
                    'rating': row['Rating'],
                    'date': row["Date"],
                },
                id=str(i),
            )
            ids.append(str(i))
            documents.append(document)

        vector_store.add_documents(documents=documents, ids=ids)