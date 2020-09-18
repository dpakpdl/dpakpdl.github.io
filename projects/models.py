from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")

    def __str__(self):
        return f"{self.title}, {self.technology}"

