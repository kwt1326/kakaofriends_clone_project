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


def csv_sync_db(req):
  """
  method = GET
  CSV Data to DB
  """
  if req.method == 'GET':
    with open('crawlResult.csv', 'r', encoding='utf-8-sig') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[0] == '#': continue
        Product.objects.create(product_name=row[1], price=int(float(row[2])), category='', img_path=row[3])
    return HttpResponse('success', status=200)
  return HttpResponse('failed', status=404)


def crawling_category_set_data(req):
  if req.method == 'POST':
    character = req.POST.get('character')
    page = 1
    url = "https://store.kakaofriends.com/api/category/goods/23?t=1604450345178&sort=createDatetime,desc&page={0}&size=40&global=false"
    headers = {
      "referer":"https://store.kakaofriends.com/kr/products/category/character?categorySeq=23&sort=createDatetime,desc",
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
      "cookie":"",
      "accept-language": "kr",
    }


def get_kakaofriends_crawling_all(req):
  """
  method = GET
  카카오페이지 전체 카테고리 제품명, 가격, 이미지 경로 크롤링
  """
  if req.method == 'GET':
    page = 1
    url = "https://store.kakaofriends.com/api/category/goods/3?t=1604155183856&sort=createDatetime,desc&page={0}&size=40&global=false"
    headers =  {
      "referer":"https://store.kakaofriends.com/kr/products/category/subject?sort=createDatetime,desc",
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
      "cookie":"SESSION=b50f1cb3-5253-4037-8952-7322a32288ec; AVAP1A417248742=1604208891058396255%7C2%7C1604208891058396255%7C1%7C1604208891806NCX58; Trkses_AP1A417248742=1604208891058396255; TOKEN=eyJ0eXAiOiJKV1QiLCJyZWdEYXRlIjoxNjA0MjA4OTAyMzMzLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiNTBmMWNiMy01MjUzLTQwMzctODk1Mi03MzIyYTMyMjg4ZWMiLCJjbGllbnRTZWNyZXQiOiJiNTBmMWNiMy01MjUzLTQwMzctODk1Mi03MzIyYTMyMjg4ZWMiLCJST0xFIjoiQU5PTllNT1VTX1VTRVIiLCJLQUtBT19NRU1CRVJfWU4iOiJOIiwiZXhwIjoxNjA0MjA5NTAyfQ.ricCiStuh_4VILNJd1d1Gx9Uxzmp7oP8bhn5JgkdV24; _ga=GA1.2.1240753300.1604208892; _gid=GA1.2.1424900098.1604208892; _gat=1; _fbp=fb.1.1604208892129.278497594; XSRF-TOKEN=1e31ffec-015a-4fd0-aaa0-ca46828b7300; SCOUTER=z2t102q8n2htec; friends=B44BC2B9BE634DB7C614BDA4C7760497; ASAP1A417248742=1604208891058396255%7C1604208901031821231%7C1604208891058396255%7C0; ARAP1A417248742=https%3A//store.kakaofriends.com/kr/products/category/subject%3Fsort%3DcreateDatetime%2Cdeschttps%3A//store.kakaofriends.com/kr/index%3Ftab%3Dhome; _T_ANO=COdkrt8zDQinheI2+8yZ2oJ++nucnuN12CxtCr6/9wKOkpnmm820ABZiPdkdMmz0fiXjKww11JZmQIjj8ulfGqup2En4+isMYtEyOO6IB7Fxe/OLuJ4i7hWhRL/LzQUFvQzunBvYnnGiXQDMg7cCMAys7yCQJU9zUy4hiT+siFzxSJEtoORbFt6FYI9bXGfEM9GhOFt0n/kxJrA5IrLKOfUEMkqhbngMnn1trzwNW9MzvTk2Qiwt+SkRNmV+JDGPeuxibhqu9j74yjxIqCH7x9Z+20UkJgBuBzPGhszd5qFaSeCLTq1SNTobR+xdqL5M0SsTi+LVmqibDeNIp059vw==",
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
    title_list = soup.find_all("p", class_="item__ItemTitle-sc-5t2pho-2 bYxEAu")
    price_list = soup.find_all("span", class_="item__ScreenOut-sc-5t2pho-7 fKUbEJ")
    img_list = soup.find_all("span", class_="img__Wrap-sc-1ck9vd1-0 eBXedy")
    img_name_list = []
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