"""Data Processor."""
import pandas as pd
from typing import List, Dict

class DataProcessor:
    
    def __init__(self, df: pd.DataFrame):
        self._df: pd.DataFrame = df

    def aggregate_statistics_for_documents(self) -> List[Dict]:
        """Compute all statistics for passing to vector store."""
    
        