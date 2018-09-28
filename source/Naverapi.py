# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import json
import re
import requests

# 네이버 검색 Open API 사용 요청시 얻게되는 정보를 입력합니다
naver_client_id = "5JqeEHVs2ELDkAbseokq"
naver_client_secret = "wIZdiGl2fA"


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def searchByTitle(title):
    myurl = 'https://openapi.naver.com/v1/search/movie.json?display=100&query=' + quote(title)
    request = urllib.request.Request(myurl)
    request.add_header("X-Naver-Client-Id", naver_client_id)
    request.add_header("X-Naver-Client-Secret", naver_client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        d = json.loads(response_body.decode('utf-8'))
        if (len(d['items']) > 0):
            return d['items']
        else:
            return None

    else:
        print("Error Code:" + rescode)


def findcodeByInput(items):
    for index, item in enumerate(items):
        naverlink = cleanhtml(item['link'])
        print(naverlink)
        naverid = re.split("code=", naverlink)[1]

        return naverid



def getCodeFromNaver(searchTitle):
    items = searchByTitle(searchTitle)

    if (items != None):
        return findcodeByInput(items)
    else:
        print("No result")


#getCodeFromNaver(u"블랙팬서")