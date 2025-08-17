from contextlib import contextmanager

from django.db import transaction


class UnitOfWork:
    def __init__(self):
        self.repositories = {}

    @contextmanager
    def __call__(self):
        with transaction.atomic():
            yield self
            # Commit implicit
