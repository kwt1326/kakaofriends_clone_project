from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project_app import models, serializers
from .queries.product import *

class ProductView(APIView):
  """
  Product CRUD API
  """
  
  permission_classes = (permissions.AllowAny,)

  def get(self, request):
    page = request.query_params.get('page')
    per_page = request.query_params.get('per_page')
    if int(page) <= 0: page = 1

    product_list = models.Product.objects.raw(GET_LIST_PRODUCT.format((int(page) - 1) * int(per_page), int(per_page)))
    serializer = serializers.ProductSerializer(product_list, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = serializers.ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
