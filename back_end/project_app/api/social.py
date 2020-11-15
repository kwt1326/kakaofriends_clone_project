import requests
import json, urllib

from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from django.contrib.auth.hashers import make_password, check_password

from project_app.common import response, constant
from project_app.common.response import AppResponse


'''
https://developers.naver.com/docs/login/api/
https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api

http://localhost:8888/accounts/naver/login/callback
http://localhost:8888/accounts/kakao/login/callback
'''


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def login(request, social):
    result = response.result(request.path)

    social = social.upper()

    if social_check(social) != True:
        result['message'] = social_check(social)
        return AppResponse(result)

    AUTH_URL = eval(f'constant.{social}_AUTH_URL')
    CLIENT_ID = eval(f'constant.{social}_CLIENT_ID')
    CALLBACK_URL = eval(f'constant.{social}_CALLBACK_URL')

    api_url = f'''{AUTH_URL}?\
        client_id={CLIENT_ID}&\
        redirect_uri={CALLBACK_URL}&\
        response_type=code&\
        state=state'''

    api_url = api_url.replace(' ', '')

    result['code'] = 'SUCCESS'
    result['object'] = { 'url': api_url }

    # 프론트에서 팝업으로
    return AppResponse(result)


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def login_callback(request, social):
    result = response.result(request.path)

    social = social.upper()

    if social_check(social) != True:
        result['message'] = social_check(social)
        return AppResponse(result)

    TOKEN_URL = eval(f'constant.{social}_TOKEN_URL')
    CLIENT_ID = eval(f'constant.{social}_CLIENT_ID')
    GRANT_TYPE = eval(f'constant.{social}_GRANT_TYPE')
    SECRET_KEY = eval(f'constant.{social}_SECRET_KEY')

    try:
        url = TOKEN_URL
        data = {
            'grant_type': GRANT_TYPE,
            'client_id': CLIENT_ID,
            'client_secret': SECRET_KEY,
            'code': request.GET.get('code'),
        }

        obj = requests.post(url, data = data)

        print(obj.text)

        if 'error' in obj.text:
            print(obj.text)
            result['message'] = '다시 시도해 주세요.'
            return AppResponse(result)

    except Exception as e:
        print(request.path)
        print(e)
        result['message'] = '[e] 다시 시도해 주세요.'

    '''
    token_type
    access_token
    refresh_token
    expires_in
    refresh_token_expires_in

    프론트로 토큰을 보내서 처리 아니면 백에서 전부 처리

    + 메일 디비 등록
    ++ jwt
    '''

    result['code'] = 'SUCCESS'

    return AppResponse(result)


def social_check(social):
    social = social.upper()

    if social in ['NAVER', 'KAKAO', 'GOOGLE']:
        return True

    return '오류 메시지 수정'
