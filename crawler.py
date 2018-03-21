import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'bazha.settings'
django.setup()

import requests
from crawler.langconv import *
import time
from bs4 import BeautifulSoup
from News.models import Article, Article_Part

#last_title = ''

def chinese_to_gb2312(chinese):
    s = str(chinese.encode('gb2312')).replace('\\x', '')
    return s.replace("'", '')[1:].upper()

def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

def save_img(src,name):
    ir = requests.get(src)
    if ir.status_code == 200:
        open('Main/static/Main/img/News/' + name + '.jpg', 'wb').write(ir.content)
    else:
        return 0
    return 1

def save_article(url, title, title_img_src):

    title = title.replace('/','').replace('\\','')
    title_img_name = chinese_to_gb2312(title).replace(' ','').replace('\\','')
    article_list = []
    a = Article.objects.filter(title = title)
    if len(a) == 1:
        return

    resp = requests.get(url)
    bsobj = BeautifulSoup(resp.text, 'lxml')
    article = bsobj.find_all('div',class_ = 'single-container')[0]
    divs = article.find_all('div')

    for d in divs:
        for c in d.children:
            try:
                if 'gallery' in c['id']:
                    a = d
            except:
                pass

    for c in a.children:
        try:
            if 'gallery' in c['id']:
                article_list.append(c)
                continue
        except:
            pass
        if c.name == 'p':
            article_list.append(c)

    if not save_img(title_img_src,title_img_name):
        return

    A = Article(title = title, title_img = 'News/'+title_img_name +'.jpg')
    A.save()
    for m,i in enumerate(article_list):
        if i.name == 'p':
            A_P = Article_Part(text=cht_to_chs(i.text), belong_to = A,order = m)
            A_P.save()
        else:
            src = i.find('img')['src']
            img_name = str(A.pk) + '_' + str(m)
            if not save_img(src, img_name):
                continue
            A_P = Article_Part(img='News/' + img_name + '.jpg', belong_to=A, order=m)
            A_P.save()

    print('保存完毕')
    #print(divs)

def test_new():

    resp = requests.get('https://kenlu.net/category/news/')
    bsobj = BeautifulSoup(resp.text, 'lxml')
    first_new = bsobj.find_all('div', class_='mg-col mg-col-1')[0]
    title = cht_to_chs(first_new.h2.text)

    a_img = first_new.a.get('data-src')
    href = first_new.a.get('href')
    save_article(url=href, title=title, title_img_src=a_img)


if __name__ == '__main__':
    while True:
        try:
            test_new()
        except:
            pass
        time.sleep(60)