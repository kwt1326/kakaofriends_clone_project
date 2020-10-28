from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

import allauth
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from project_app.api import auth, social, user


router = DefaultRouter()
router = SimpleRouter(trailing_slash=True)

router.register(r'^auth/email', auth.EmailViewSet, basename='auth-email--post')
router.register(r'^auth/email/(?P<email>[\w.-]+@[a-zA-Z0-9.-_]+\.[a-zA-Z.]+)',
  auth.EmailViewSet, basename='auth-email--get')
router.register(r'^auth/join', auth.JoinViewSet, basename='auth-join--post')
router.register(r'^auth/login', auth.LoginViewSet, basename='auth-login--post')

router.register(r'^user', user.UserViewSet, basename='user')


urlpatterns = [
  path('auth/login/<str:social>', social.login),
  path('auth/login/<str:social>/callback', social.login_callback),

  path('auth/token', obtain_jwt_token),
  path('auth/token-refresh', refresh_jwt_token),
  path('auth/token-verify', verify_jwt_token),

  # 순서 주의
  path('', include(router.urls)),
  #path('accounts/', include('allauth.urls')),
]
