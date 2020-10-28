from django.urls import path, include
from project_app import views

from project_app.api.others import *
from project_app.api.product import ProductView

urlpatterns = [
  path('crawl_kakaopage', get_kakaofriends_crawling),
  path('product', ProductView.as_view())
]