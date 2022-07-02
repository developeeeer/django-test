from django.db import models

from todo.managers import TodoManager

class ToDo(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=20, db_column="title")
    detail = models.CharField("name", max_length=20, db_column="description")
    
    objects = TodoManager()

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"
        ordering = ("id",)

    def __str__(self):
        return self.name