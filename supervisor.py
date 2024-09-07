import logging
from adapter import LLMAdapter

logger = logging.getLogger(__name__)

class Supervisor:
    def __init__(self):
        self.adapter = LLMAdapter()

    def handle_query(self, query):
        logger.info(f"Handling query: {query}")
        response = self.adapter.process_query(query)
        recommendations = self.adapter.recommend_resources(query)
        return response, recommendations

