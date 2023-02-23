from django.db import models

class MyModel(models.Model):
    col1 = models.CharField(max_length=50)

class MyModelDate(models.Model):
    col2 = models.DateTimeField()