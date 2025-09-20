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
            self._income_by_region(),
        ]
        return aggregated_documents
    
    def _income_by_payment(self) -> Dict:
        """Aggregate income by payment method."""
        income_by_payment = self._df.groupby('Payment_Method')['Earnings_USD'].agg([
            'mean', 'median', 'count', 'std',
        ]).round(2).to_dict()
        return {
            'page_content': f'Сравнение доходов фрилансеров по способу оплаты {str(income_by_payment)}',
        }
        
    def _income_by_region(self) -> Dict:
        """Aggregate income by region."""
        income_by_region = self._df.groupby('Client_Region')['Earnings_USD'].agg([
            'mean', 'median', 'count', 'std'
        ]).round(2).to_dict()
        return {
            'page_content': f'Сравнение доходов фрилансеров по региону проживания {str(income_by_region)}',
        }
    
    
        
    
    
        