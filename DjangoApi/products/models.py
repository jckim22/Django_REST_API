from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=30, blank=False, default='')
    comment = models.CharField(max_length=300, blank=False, default='')
