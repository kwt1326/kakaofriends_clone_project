from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup
import requests

def get_kakaofriends_crawling(req):
  # request = requests.get('https://store.kakaofriends.com/kr/products/category/subject?sort=createDatetime,desc')
  # soup = BeautifulSoup(request.text, 'html.parser')

  # deps1 = soup.find(id="kakaoWrap")
  # deps2 = deps1.find(id="kakaoContent")
  # deps3 = deps2.find(id="cMain")
  # deps4 = deps3.find(id="mArticle")

  # product_title_data = soup.find_all("p", class_="item__ItemTitle-sc-5t2pho-2 bYxEAu")
  # product_img_data = soup.find_all("img")
  # price_data = soup.find_all("p", alt="item__Price")

  print(request.content)
  print(request.json)

  return None # JsonResponse(soup, status=200)