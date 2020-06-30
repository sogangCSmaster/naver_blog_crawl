import requests
import json
from bs4 import BeautifulSoup
import sys

#keyword = sys.argv[1]
#page = sys.argv[2]

keyword = "논현 맛집"
page = 3
print(keyword, page)

search_url = "https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&sm=tab_pge&srchby=all&st=sim&where=post&query=" + keyword

hrefList = []

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

for href in hrefList:
    res = requests.get(href)
    html = res.text
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {'class': 'se-main-container'})
    content = content.text
    print(content)
