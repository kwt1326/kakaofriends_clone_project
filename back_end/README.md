# API

- [Auth](#auth)
- [User](#user)


**common response**

```json
{
  "api":"",
  "code": "SUCCESS",
  "message": "",
  "object": {
      "key" : ""
  }
}

# error
{
  "api":"",
  "code": "ERROR",
  "message": "",
  "object": {
      "error": {
          "key" : ""
      }
  }
}
```


## Auth

- [이메일 등록](#이메일-등록)
- [이메일 조회](#이메일-조회)
- [회원 가입](#회원-가입)
- [로그인](#로그인)


### 이메일 등록

POST `/api/auth/email`

구분 | 속성 | 타입 | 필수 여부 | 기타
---|---|---|:---:|---
body   | email | string | o | unique



### 이메일 조회

GET ` /api/auth/email/<test@example.com>`

! 한글 이메일 안됨   
! 숫자로 시작하는 이메일 안됨   



### 회원 가입

POST `/api/auth/join`

구분 | 속성 | 타입 | 필수 여부 | 기타
---|---|---|:---:|---
body   | email | string | o | unique
body   | password | string | o | min 5 ~ max 50


### 로그인

POST `/api/auth/login`

구분 | 속성 | 타입 | 필수 여부 | 기타
---|---|---|:---:|---
body   | email | string | o | unique
body   | password | string | o | min 5 ~ max 50


**네이버 로그인**   
GET `/api/auth/login/naver`

**카카오 로그인**  
GET `/api/auth/login/kakao`



---
### 토큰

`auth/token`   

180초



### 토큰 재할당

POST `auth/token-refresh`

! 토큰 1시간

구분 | 속성 | 타입 | 필수 여부 | 기타
---|---|---|:---:|---
body   | email | string | o | unique
body   | password | string | o | min 5 ~ max 50
body   | token | string | o |

```json
request
{
  "email":"",
  "password":"",
  "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InRlc3QxMjNAdGVzdC5jb20iLCJleHAiOjE2MDQ3MTcyODQsImVtYWlsIjoidGVzdDEyM0B0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNjA0NzE3MTA0fQ.TE5CE-R_R_hTraxRsJZgsCh_Ppq8OVm6U6oSHmhOFiQ"
}
```





구분 | 속성 | 타입 | 필수 여부 | 기타
---|---|---|:---:|---
header   | Authorization | string | o | jwt <token>
