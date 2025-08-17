from django.urls import path

from .views import KnowledgeListCreateView

urlpatterns = [
    path('workspaces/<int:workspace_id>/', KnowledgeListCreateView.as_view(), name='knowledge-list-create'),
]
