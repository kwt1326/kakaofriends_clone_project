from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _


'''
some = validators.RegexValidator(
    r'^[\w.@+-]+$',
    _('유효성 오류'),
    code='invalid'
)
'''

@deconstructible
class Min(object):
    def __init__(self, min):
        self.min = min

    def __call__(self, value):
        if len(value) < self.min:
            raise ValidationError( _(f'{self.min} 글자 이상 입력하세요.'), code='invalid')
        else:
            return value


@deconstructible
class Max(object):
    def __init__(self, max):
        self.max = max

    def __call__(self, value):
        if len(value) > self.max:
            raise ValidationError( _(f'{self.max} 글자 이하로 입력하세요.'), code='invalid')
        else:
            return value
