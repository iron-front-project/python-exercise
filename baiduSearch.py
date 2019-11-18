# -*- coding:utf-8 -*-
import requests
import re
from pyquery import PyQuery as pq

def baiduSearch():


    url = "https://www.baidu.com/s?"
    data = {
      'wd': '薛刚',
    }
	# 组建 url
	url = url + urlencode(data)

    response = requests.get(url)

    doc = pq(response.text)

    lists = doc("#content_left h3.t a").items()

    for list in lists:
        title = list.text()
        link = list.attr("href")
        print('标题：' + title)
		print('链接：' + link)

if __name__ == "__main__":
    baiduSearch()