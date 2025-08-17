from abc import ABC, abstractmethod

from django.db.models import Model


class BaseRepository(ABC):
    def __init__(self, model: Model):
        self.model = model

    @abstractmethod
    def add(self, instance):
        pass

    @abstractmethod
    def get(self, pk):
        pass

    # TODO Add get_all, update, delete as needed


class DjangoRepository(BaseRepository):
    def add(self, instance):
        instance.save()

    def get(self, pk):
        return self.model.objects.get(pk=pk)
