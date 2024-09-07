import logging
from llm_layer import LLM

logger = logging.getLogger(__name__)

class LLMAdapter:
    def __init__(self):
        self.llm = LLM()

    def process_query(self, query):
        logger.info(f"Processing query: {query}")
        response = self.llm.generate_response(query)
        return response

    def recommend_resources(self, query):
        logger.info(f"Recommending resources for query: {query}")
        recommendations = self.llm.suggest_resources(query)
        return recommendations
