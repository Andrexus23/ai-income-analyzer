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
            self._get_projects_count_of_freelancers_with_level(
                level="Expert", 
                page_content='Фрилансеры, считающие себя экспертами, выполнили столько проектов',
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
    
    def _get_projects_count_of_freelancers_with_level(self, level: str, page_content: str):
        """Get freelancers with condition."""
        relevant_part: List = list(self._df[self._df['Experience_Level'] == level]['Job_Completed'].to_dict().values())
        return {
            'page_content': f'{page_content} (всего {len(relevant_part)}, через запятую): {str(relevant_part)}',
        }
    
    
        
    
    
        