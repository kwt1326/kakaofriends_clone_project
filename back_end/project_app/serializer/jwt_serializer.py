from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class AppJWTSerializer(JSONWebTokenSerializer):
    pass

# https://stackoverflow.com/questions/34332074/django-rest-jwt-login-using-username-or-email
# https://stackoverflow.com/questions/56978424/django-rest-framework-custom-jwt-authentication
