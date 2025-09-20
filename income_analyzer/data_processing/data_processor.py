"""Data Processor."""
import pandas as pd
from typing import List, Dict

class DataProcessor:
    
    def __init__(self, df: pd.DataFrame):
        self._df: pd.DataFrame = df

    def aggregate_statistics_for_documents(self) -> List[Dict]:
        """Compute all statistics for passing to vector store."""
        aggregated_documents = [
            self._income_by_payment(),
        ]
        return aggregated_documents
    
    def _income_by_payment(self):
        """Aggregate income by payment method."""
        income_by_payment = self._df.groupby('Payment_Method')['Earnings_USD'].agg([
            'mean', 'median', 'count', 'std',
        ]).round(2).to_dict()
        return {
            'page_content': f'Сравнение доходов фрилансеров по способу оплаты {str(income_by_payment)}',
            'metadata': '',
        }
    
    
        
    
    
        