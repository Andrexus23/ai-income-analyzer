"""LLM Manager, connect with LLM via API, invokes chain: prompt -> model."""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from income_analyzer.config import get_config


class LLMManager:

    def __init__(self):
        self._temperature: float = 0.1 # for statistics low temperature is better
        self.model: ChatOpenAI = self._initialize_model()
        self.prompt_template: ChatPromptTemplate = self._create_prompt_template()
        self.chain = self.prompt_template | self.model
    
    def _initialize_model(self):
        """Initialize model via API."""
        return ChatOpenAI(
            model=get_config().llm_settings.model,
            openai_api_key=os.getenv("LLM_API_KEY"),
            openai_api_base=get_config().llm_settings.api_base,
            temperature=self._temperature,
        )
        
    def _create_prompt_template(self) -> ChatPromptTemplate:
        """Create prompt for llm."""
        template: str = """
        Ты - аналитик данных, который отвечает на вопросы статистического характера о доходах фрилансеров.
        Релевантные элементы набора данных: {relevant_items}
        
        Вопрос, на который следует ответить: {question}

        Предоставь полезный и точный ответ, основанный на релевантных элементах. 
        Ответ должен содержать конкретные числа.
        Если данных недостаточно - сообщи.
        """
        return ChatPromptTemplate.from_template(template)
        
