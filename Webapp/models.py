from django.db import models
from datetime import datetime


class BooksLibrary(models.Model):
    Author=models.CharField(max_length=20)
    Title=models.CharField(max_length=20)
    Description=models.TextField()
    Created=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.Author

