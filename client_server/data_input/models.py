from django.db import models

class Item(models.Model):
    data = models.CharField(max_length=100)
