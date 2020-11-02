from django.conf import settings
from django.db import models
from django.utils import timezone

class Product(models.Model):
  product_name = models.TextField(null=False)
  price = models.IntegerField(default=0, null=False)
  category = models.CharField(max_length=20, null=False, default='others')
  character = models.CharField(max_length=10, null=True)
  img_path = models.TextField(null=True)