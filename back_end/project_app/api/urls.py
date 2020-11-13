from django.urls import path, include

from .product import ProductView
from .others import (
  crawling_category_set_data,
  get_kakaofriends_crawling_all,
  csv_sync_db,
  ping,
  )

urlpatterns = [
  path('ping', ping),
  path('crawl_kakaopage', get_kakaofriends_crawling_all),
  path('csv_to_db', csv_sync_db),
  path('product', ProductView.as_view())
]