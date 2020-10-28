from rest_framework import viewsets, serializers
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view

from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone

from project_app.model import user_model
from project_app.serializer import auth_serializer
from project_app.common import response
from project_app.common.response import AppResponse


class EmailViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(EmailViewSet, self).dispatch(request, *args, **kwargs)

    def create(self, request):
        result = response.result(request.path)

        serializer = auth_serializer.EmailSerializer(data=request.data)

        if not serializer.is_valid():
            result['object'] = { 'error': serializer.errors }
            return AppResponse(result)

        # + 이메일 인증

        try:
            user = user_model.User(email=request.data['email'])
            user.save()

            result['code'] = 'SUCCESS'
            result['message'] = '메일을 등록했습니다.'
            result['object'] = { 'email' : user.email }

        except Exception as e:
            print(request.path)
            print(e)
            result['message'] = '다시 시도해 주시기 바랍니다.'

        return AppResponse(result)

    def list(self, request, email=None):
        result = response.result(request.path)

        user = user_model.User.objects.filter(email=email)

        if not user:
            result['code'] = 'SUCCESS'
            result['message'] = '해당하는 메일이 없습니다.'
            result['object'] = { 'email' : 'null' }

        else:
            result['message'] = '사용중인 메일입니다.'
            result['object'] = { 'email' : user.email }

        return AppResponse(result)


class JoinViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(JoinViewSet, self).dispatch(request, *args, **kwargs)

    def create(self, request):
        result = response.result(request.path)

        serializer = auth_serializer.JoinSerializer(data=request.data)

        if not serializer.is_valid():
            result['object'] = { 'error': serializer.errors }
            return AppResponse(result)

        email = request.data['email']
        password = make_password(request.data['password'])

        try:
            user = user_model.User(email=email, password=password)
            user.save()

            result['code'] = 'SUCCESS'
            result['message'] = '회원 가입 완료'
            result['object'] = { 'email' : user.email }

        except Exception as e:
            print(request.path)
            print(e)
            result['message'] = '회원 가입 실패'

        return AppResponse(result)


class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        result = response.result(request.path)

        serializer = auth_serializer.LoginSerializer(data=request.data)

        if not serializer.is_valid():
            result['object'] = { 'error': serializer.errors }
            return AppResponse(result)

        email = request.data['email']
        password = request.data['password']

        try:
            user = user_model.User.objects.get(email=email)

        except user_model.User.DoesNotExist:
            result['message'] = '가입하지 않은 이메일입니다.'
            return AppResponse(result)

        if check_password(password, user.password):

            user.logined_at = timezone.now()
            user.save()

            # jwt
            # 토큰 발급을 리다이렉트로?
            #serializer = auth_serializer.LoginSerializer(user)
            #print(serializer.data)

            result['code'] = 'SUCCESS'
            result['message'] = '로그인 성공'
            result['object'] = {
                'token' : 'token.key',
            }

        else:
            result['message'] = '로그인 실패'

        return AppResponse(result)
