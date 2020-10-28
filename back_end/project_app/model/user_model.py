from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from project_app.utils import validate
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
  uno = models.AutoField(primary_key=True)
  email = models.EmailField(unique=True)
  second_email = models.EmailField(null=False, default='')
  password = models.TextField(validators=[validate.Min(5), validate.Max(50)])
  social_login = models.CharField(max_length=100, default='')
  state = models.BooleanField(null=False, default=True)
  logined_at = models.DateTimeField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  deleted_at = models.DateTimeField(null=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'

  class Meta:
    verbose_name = _('app_user')
    verbose_name_plural = _('app_users')
    ordering = ['uno']


class Profile(models.Model):
  pno = models.AutoField(primary_key=True)
  uno = models.OneToOneField('User', to_field='uno', on_delete=models.CASCADE)
  name = models.CharField(max_length=30, null=False, default='')
  gender = models.IntegerField(null=False, default=0)
  birthday = models.CharField(max_length=10, null=False, default='')
  profile_img_url = models.TextField(null=False, default='')
  ad_accept_yn = models.BooleanField(null=False, default=True)

  class Meta:
    db_table = 'project_app_user_profile'


class Address(models.Model):
  ano = models.AutoField(primary_key=True)
  uno = models.ForeignKey('User', to_field='uno', on_delete=models.CASCADE)
  name = models.CharField(max_length=50, null=False, default='')
  address_title = models.CharField(max_length=60, null=False, default='')
  address1 = models.TextField(null=False, default='')
  address2 = models.TextField(null=False, default='')
  zip_code = models.CharField(max_length=10, null=False, default='')
  phone_number = models.CharField(max_length=15, null=False, default='')
  second_phone_number = models.CharField(max_length=15, null=False, default='')
  default_address_yn = models.BooleanField(null=False, default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'project_app_user_address'
