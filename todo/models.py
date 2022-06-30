from django.db import models

class ToDo(models.Model):
    id = models.AutoField("id", primary_key=True)
    name = models.CharField("name", max_length=20, db_column="title")
    detail = models.CharField("name", max_length=20, db_column="description")

    class Meta:
        verbose_name = "ToDo"
        verbose_name_plural = "ToDo"
        ordering = ("id",)

    def __str__(self):
        return self.name