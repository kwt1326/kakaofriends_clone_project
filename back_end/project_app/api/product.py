from rest_framework import viewsets
from rest_framework import permissions
from project_app import models, serializers

class ProductViewSet(viewsets.ModelViewSet):
  """
  Product REST API
  """
  queryset = Product.object.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticated]