from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator

from project_app.model import user_model


class EmailSerializer(serializers.ModelSerializer):
  class Meta:
    model = user_model.User
    fields = ('email',)


class JoinSerializer(serializers.ModelSerializer):
  class Meta:
    model = user_model.User
    fields = ('email', 'password',)


class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = user_model.User
    fields = ('email', 'password',)
    read_only_fields = ('uno', 'state', 'created_at', )
    extra_kwargs = {
        'email': {
            'validators': [ UnicodeUsernameValidator() ],
        }
    }
