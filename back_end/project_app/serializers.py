from rest_framework import serializers
from project_app.models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    fields = ['id', 'product_name', 'price', 'category']