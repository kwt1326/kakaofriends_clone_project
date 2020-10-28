from django.conf import settings
from django.db import models
from django.utils import timezone

class Product(models.Model):
  product_name = models.CharField(max_length=20, null=False)
  price = models.SmallIntegerField(default=0, null=False)
  category = models.CharField(max_length=20, null=False, default='others')
  img_path = models.TextField(null=True)