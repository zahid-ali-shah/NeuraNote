from rest_framework import serializers

from apps.knowledge.models import Knowledge


class KnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
