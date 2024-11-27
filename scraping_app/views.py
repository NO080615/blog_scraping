from django.shortcuts import render
#ライブラリをインポート
import requests
from bs4 import BeautifulSoup

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

# 参考サイト
# https://techplay.jp/column/601
def scraping(request):
# スクレイピング
    url="http://127.0.0.1:8000/scraping_app/"
    res = requests.get(url)
    html = res.text
    print("res: ", html)
    soup = BeautifulSoup(html, "html.parser")
    time = soup.select(".waitingtime")
    print("title: ", time)
    return HttpResponse(time)
