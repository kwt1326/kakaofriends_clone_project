"""
Django settings for project_server project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os, sys
import json
import datetime


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR.parent, 'env/local_env.json'), 'r') as f:
  config = json.load(f)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8yui54p0twusy-9ln5c7^)!b7k^on)q7&h1r@43)jd0(tei@6+'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'rest_framework.authtoken',
  'corsheaders',
  'project_app',
  # 추가
  'django.contrib.sites',
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  'allauth.socialaccount.providers.naver',
  'allauth.socialaccount.providers.kakao',
  'allauth.socialaccount.providers.google',
]

# https://docs.djangoproject.com/en/3.1/ref/middleware/
MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  # 추가
  'project_app.middleware.SomeMiddleware',

]

# Rest -- 위치 변경
REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated',
  ],
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
  ],
  'DEFAULT_RENDERER_CLASSES': [
    'rest_framework.renderers.JSONRenderer',
  ],
  'DEFAULT_PARSER_CLASSES': [
    'rest_framework.parsers.JSONParser',
  ],
}

REST_USE_JWT = True

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'project_app.User'


# 추가
# JWT
# https://jpadilla.github.io/django-rest-framework-jwt/

JWT_AUTH = {
  'JWT_SECRET_KEY': '테스트임시키',
  'JWT_GET_USER_SECRET_KEY': None,
  'JWT_PUBLIC_KEY': None,
  'JWT_PRIVATE_KEY': None,
  'JWT_ALGORITHM': 'HS256',
  'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=180),
  'JWT_ALLOW_REFRESH': True,
  'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=1),
}

# JWT_RESPONSE_PAYLOAD_HANDLER


ROOT_URLCONF = 'project_server.urls'

TEMPLATES = [{
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [os.path.join(BASE_DIR.parent, 'front_end/build')],
  'APP_DIRS': True,
  'OPTIONS': {
      'context_processors': [
      'django.template.context_processors.debug',
      'django.template.context_processors.request',
      'django.contrib.auth.context_processors.auth',
      'django.contrib.messages.context_processors.messages',
    ],
  },
},]

STATICFILES_DIRS = [
  os.path.join(BASE_DIR.parent, 'front_end/build/static')
]

WSGI_APPLICATION = 'project_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = config['LOCAL_ENV_DATABASES']


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
  'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
  'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  'OPTIONS': {'min_length': 5,}
  },
  {
  'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
  'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# 수정
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False

#LANGUAGE_CODE = 'en-us'
#TIME_ZONE = 'UTC'
#USE_TZ = True

USE_I18N = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# Cors
# https://pypi.org/project/django-cors-headers/3.5.0/

CORS_ALLOW_HEADERS = (
  'content-type',
  'csrftoken',
  'authorization',
  '___internal-request-id', # Talend API test
)

CORS_ORIGIN_ALLOW_ALL = True

'''
CORS_ORIGIN_WHITELIST = (
  'http://localhost:3000', # React local-dev domain
)
'''

CORS_ALLOW_CREDENTIALS = True # 자격 증명 허용 ( 프론트에서 Axios 로 요청 보낼때 withCredition 을 사용하는 것에 대응 )

CSRF_COOKIE_NAME = 'csrftoken'


# 추가
APPEND_SLASH = True
