from core.infrastructure.services import BaseService
from core.infrastructure.uow import UnitOfWork

from .models import Knowledge
from .repositories import KnowledgeRepository


class KnowledgeService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow)
        self.knowledge = KnowledgeRepository()

    def create_knowledge(self, data):
        with self.uow():
            knowledge = Knowledge(**data)
            self.knowledge.add(knowledge)
            return knowledge

    # Stub for AI integration (post-MVP)
    def extract_from_document(self, doc_path, existing_topic):
        # Use LlamaIndex/LangChain/Ollama to parse PDF/website and create knowledge similar to existing (e.g., Django -> Python)
        pass  # Implement: index = DirectoryReader(doc_path).load_data(); ... create_knowledge
