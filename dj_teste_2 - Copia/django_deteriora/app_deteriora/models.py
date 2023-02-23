from django.db import models

from datetime import date

class MyModelDateHj(models.Model):
    col3 = models.DateField()

class MyModelDateHj2(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)