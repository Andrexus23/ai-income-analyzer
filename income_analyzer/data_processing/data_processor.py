"""Data Processor."""
import pandas as pd
from typing import List, Dict

class DataProcessor:
    
    def __init__(self, df: pd.DataFrame):
        self._df: pd.DataFrame = df

    def aggregate_statistics_for_documents(self) -> List[Dict]:
        """Compute all statistics for passing to vector store."""
        aggregated_documents = [
            self._income_by('Payment_Method', page_content='способу оплаты'),
            self._income_by('Client_Region', page_content='региону проживания'),
            self._get_percent_of_freelancers_with_level(
                level="Expert",
                less_than=100,
                page_content='Процент фрилансеров, считающий себя экспертами, выполнивший менее 100 проектов',
            ),
        ]
        return aggregated_documents
        
    def _income_by(self, by: str, page_content: str) -> Dict:
        """Aggregate income by field."""
        income_by_field: Dict = self._df.groupby(by)['Earnings_USD'].agg([
            'mean', 'median', 'count', 'std'
        ]).round(2).to_dict()
        return {
            'page_content': f'Сравнение доходов фрилансеров по {page_content} (в $): {str(income_by_field)}',
        }
    
    def _get_percent_of_freelancers_with_level(self, level: str, less_than: int, page_content: str):
        """Get freelancers percent with specific level by Job Completed."""
        df = self._df
        relevant_part: float = round((
            df[(df['Experience_Level'] == level) & (df['Job_Completed'] < less_than)].shape[0] / 
            df[(df['Experience_Level'] == level)].shape[0]
        ) * 100, 2)
        return {
            'page_content': f'{page_content}: {str(relevant_part)} %',
        }
    
    
        
    
    
        