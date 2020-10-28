from rest_framework.response import Response


class AppResponse(Response):
  status_code = 200
  '''
  def __init__(self, mimetype=None, content_type=None, status=None):
    super().__init__(status=200)
  '''


def result(api, code=None, message=None, object=None):
  obj = {
    'api': api,
    'code': code and code or 'ERROR',
    'message': message and message or '',
    'object': object and object or {},
  }
  return obj
