from django.db import models
from util.exceptions import DoesNotExistException

class TodoManager(models.Manager):
    def get_or_exception(self, pk):
        try:
            return self.get(pk=pk)
        except self.model.DoesNotExist:
            raise DoesNotExistException()

