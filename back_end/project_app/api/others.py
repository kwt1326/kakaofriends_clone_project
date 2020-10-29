from django.http import JsonResponse, HttpResponse
from project_app.model.product import Product
from selenium import webdriver
from bs4 import BeautifulSoup
import requests, json, time

from pathlib import Path
from PIL import Image
import os, csv, uuid

from django.contrib.auth import authenticate, login, logout, models

BASE_DIR = Path(__file__).resolve().parent.parent

def get_kakaofriends_crawling(req):
  """
  method = GET
  카카오페이지 전체 카테고리 제품명, 가격, 이미지 경로 크롤링
  """

  if req.method == 'GET':
    try:
      os.stat('./images')
    except:
      os.mkdir('./images')

    page = 1
    url = "https://store.kakaofriends.com/api/category/goods/3?t=1604155183856&sort=createDatetime,desc&page={0}&size=40&global=false"

    headers =  {
      "referer":"https://store.kakaofriends.com/kr/products/category/subject?sort=createDatetime,desc",
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
      "cookie":"NEED ALWAYS UPDATE",
      "accept-language": "kr",
    }

    req_url = url.format(page)
    res = requests.get(req_url, headers=headers)
    result = json.loads(res.text)
    result_len = result["totalPages"]

    f = open('crawlResult.csv', 'w', encoding='utf-8-sig')
    wr = csv.writer(f)

    wr.writerow([u'#',u'product_name'.encode('utf-8'),u'product_price'.encode('utf-8'),u'image_path'.encode('utf-8')])

    count = 0

    for i in range(result_len):
      for j in range(len(result["content"])):
        item = result["content"][j]
        wr.writerow([str(count), item["name"], item["salePrice"], item["imageUrl"]])
        count += 1
      
      time.sleep(0.5)
      page = i + 2
      req_url = url.format(page)
      res = requests.get(req_url, headers=headers)
      result = json.loads(res.text)

    f.close()
    return HttpResponse('success') # JsonResponse(, status=200)
  return HttpResponse('failed', status=404)


def get_kakaofriends_crawling_from_browser(req):
  """
  method = GET
  카카오페이지 기본 카테고리 제품명, 가격, 이미지 크롤링
  """

  if req.method == 'GET':
    try:
      os.stat('./images')
    except:
      os.mkdir('./images')

    f = open('crawlResult.csv', 'w', encoding='utf-8-sig')
    wr = csv.writer(f)

    wr.writerow([u'#',u'product_name'.encode('utf-8'),u'product_price'.encode('utf-8'),u'image_path'.encode('utf-8')])

    driver_path = os.path.join(BASE_DIR.parent, 'utility\chromedriver.exe')
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=driver_path)
    
    driver.get('https://store.kakaofriends.com/kr/products/category/subject?sort=createDatetime,desc')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    category_list = soup.find_all("ul", itemtype="categoryProducts")
    title_list = soup.find_all("p", class_="item__ItemTitle-sc-5t2pho-2 bYxEAu")
    price_list = soup.find_all("span", class_="item__ScreenOut-sc-5t2pho-7 fKUbEJ")
    img_list = soup.find_all("span", class_="img__Wrap-sc-1ck9vd1-0 eBXedy")

    img_name_list = []

    'pagination__Page-sc-1kndqkr-1 hcZclE'

    for img_elem in img_list:
      img_src = img_elem.find_all("img")[0]['src']
      img = Image.open(requests.get(img_src, stream = True).raw)
      img_path = 'images/' + ''.join(str(uuid.uuid1()).split('-')) + '.jpg'
      img.save(img_path)
      img_name_list.append(''.join(img_path.split('/')[1]))

    for i in range(len(title_list)):
      wr.writerow([str(i), title_list[i].contents[0], price_list[i].nextSibling.contents[0], img_name_list[i]])

    f.close()
    return HttpResponse('success') # JsonResponse(soup, status=200)
  return HttpResponse('failed', status=404)