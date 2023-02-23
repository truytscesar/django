from django.db import models

class MyModel(models.Model):
    col1 = models.CharField(max_length=50)

class MyModelDate(models.Model):
    col2 = models.CharField()

import datetime

class MyModelDateHj2(models.Model):
    col3 = models.CharField(default=datetime.datetime.now)
