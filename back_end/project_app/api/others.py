from django.http import JsonResponse, HttpResponse
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

from pathlib import Path
from PIL import Image
import os, csv, uuid

from django.contrib.auth import authenticate, login, logout, models

BASE_DIR = Path(__file__).resolve().parent.parent

def get_kakaofriends_crawling(req):
  """
  method = GET
  카카오페이지 기본 카테고리 제품명, 가격, 이미지 크롤링
  """

  if req.method == 'GET':
    f = open('crawlResult.csv', 'w')
    wr = csv.writer(f)
    wr.writerow([u'#',u'product_name'.encode('utf-8'),u'product_price'.encode('utf-8'),u'image_path'.encode('utf-8')])

    driver_path = os.path.join(BASE_DIR.parent, 'utility\chromedriver.exe')
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(5)
    
    driver.get('https://store.kakaofriends.com/kr/products/category/subject?sort=createDatetime,desc')
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    category_list = soup.find_all("ul", itemtype="categoryProducts")
    title_list = soup.find_all("p", class_="item__ItemTitle-sc-5t2pho-2 bYxEAu")
    price_list = soup.find_all("span", class_="item__ScreenOut-sc-5t2pho-7 fKUbEJ")
    img_list = soup.find_all("span", class_="img__Wrap-sc-1ck9vd1-0 eBXedy")

    for i in range(len(title_list)):
      wr.writerow([str(i).encode('utf-8'),title_list[i].encode('utf-8'),price_list[i].encode('utf-8'),img_list[i].encode('utf-8')])

    for elem in title_list:
      print(elem.contents[0], flush=True)

    for elem in price_list:
      print(elem.nextSibling.contents[0], flush=True)

    for img_elem in img_list:
      img_src = img_elem.find_all("img")[0]['src']
      print(img_src, flush=True)
      img = Image.open(requests.get(img_src, stream = True).raw)
      img.save(uuid.uuid1() + '.jpg')

    f.close()
    return HttpResponse('success') # JsonResponse(soup, status=200)
  return HttpResponse('failed', status=404)