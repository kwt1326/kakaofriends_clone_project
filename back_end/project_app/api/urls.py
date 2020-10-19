from django.urls import path, include
from project_app import views

from project_app.api.others import get_kakaofriends_crawling

urlpatterns = [
  path('crawl_kakaopage', get_kakaofriends_crawling)
]