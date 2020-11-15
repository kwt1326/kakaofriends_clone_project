from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from project_app.model import user_model
from project_app.serializer import auth_serializer
from project_app.common import response
from project_app.common.response import AppResponse


class UserViewSet(viewsets.ModelViewSet):
    #authentication_classes = (JSONWebTokenAuthentication)
    #permission_classes = (IsAuthenticated,)

    def create(self, request):
        result = response.result(request.path)

        return AppResponse(result)

    def list(self, request, param=None):
        result = response.result(request.path)

        return AppResponse(result)
