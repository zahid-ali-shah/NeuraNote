from apps.knowledge.models import Knowledge


class KnowledgeRepository:
    @staticmethod
    def get_knowledge_by_id(knowledge_id):
        return Knowledge.objects.get(id=knowledge_id)

    @staticmethod
    def get_all_knowledge(workspace_id):
        return Knowledge.objects.filter(workspace_id=workspace_id)

    @staticmethod
    def create_knowledge(data, workspace_id):
        return Knowledge.objects.create(workspace_id=workspace_id, **data)

    @staticmethod
    def update_knowledge(knowledge_id, data):
        knowledge = Knowledge.objects.get(id=knowledge_id)
        for key, value in data.items():
            setattr(knowledge, key, value)
        knowledge.save()
        return knowledge

    @staticmethod
    def delete_knowledge(knowledge_id):
        knowledge = Knowledge.objects.get(id=knowledge_id)
        knowledge.delete()

