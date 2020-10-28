from rest_framework import serializers
import project_app.models as models

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Product
    fields = '__all__'