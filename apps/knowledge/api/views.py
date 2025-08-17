from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.knowledge.repositories import KnowledgeRepository
from .serializers import KnowledgeSerializer


class KnowledgeListCreateView(APIView):
    def get(self, request, workspace_id):
        knowledge_items = KnowledgeRepository.get_all_knowledge(workspace_id)
        serializer = KnowledgeSerializer(knowledge_items, many=True)
        return Response(serializer.data)

    def post(self, request, workspace_id):
        serializer = KnowledgeSerializer(data=request.data)
        if serializer.is_valid():
            knowledge = KnowledgeRepository.create_knowledge(
                serializer.validated_data, workspace_id
            )
            return Response(KnowledgeSerializer(knowledge).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
