import requests
import json
from bs4 import BeautifulSoup
import sys
import time
from selenium import webdriver

#keyword = sys.argv[1]
#page = sys.argv[2]

keyword = "논현 맛집"
page = 3
print(keyword, page)

search_url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&sm=tab_pge&srchby=all&st=sim&where=post&query=" + keyword

hrefList = []


# chromedriver path 설정
driverLocation = './chromedriver/mac/v83/chromedriver'

for p in range(int(page)):
    search = ""
    if p==0:
        search = search_url + "&start=1"
    else:
        search = search_url + "&start=" + str(p) + "1"
    print(search)
    
    res = requests.get(search)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    blogList = soup.find('div', {'class': 'blog section _blogBase _prs_blg'})
    aList = blogList.find_all('a', {'class': 'sh_blog_title _sp_each_url _sp_each_title'})
    for a in aList:
        href = a['href']
        hrefList.append(href)

driver = webdriver.Chrome(driverLocation)

for href in hrefList:
    res = driver.get(href)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    src = soup.find('iframe', {'id': 'mainFrame'})
    src = src['src']
    post = "http://blog.naver.com" + src
    blogContent = requests.get(post)
    blogContent = blogContent.text
    soup = BeautifulSoup(blogContent, 'html.parser')
    content = soup.find('div', {'class': 'se-main-container'})
    content = content.text
    print(content)
