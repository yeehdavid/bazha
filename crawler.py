import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'bazha.settings'
django.setup()

import requests
from crawler.langconv import *
import time
from bs4 import BeautifulSoup
from News.models import Article, Article_Part
from PIL import Image
#last_title = ''

def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout, type)

def chinese_to_gb2312(chinese):
    s = str(chinese.encode('gb18030')).replace('\\x', '')
    return s.replace("'", '')[1:].upper()

def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

def save_img(src,name,resharp = False):
    ir = requests.get(src,timeout=10)
    if ir.status_code == 200:
        img_path = 'static/img/News/' + name + '.jpg'

        open(img_path, 'wb').write(ir.content)
        if resharp:
            ResizeImage(img_path, img_path, 750, 430, 'jpeg')

    else:
        return 0
    return 1

def save_article(url, title, title_img_src):

    title = title.replace('/','').replace('\\','')
    title_img_name = chinese_to_gb2312(title).replace(' ','').replace('\\','')
    article_list = []
    a = Article.objects.filter(title_img = 'News/'+title_img_name +'.jpg')
    if len(a) != 0:
        return

    resp = requests.get(url,timeout=10)
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
    try:
        for c in a.children:
            try:
                if 'gallery' in c['id']:
                    article_list.append(c)
                    continue
            except:
                pass
            if c.name == 'p':
                article_list.append(c)
    except:
        return 

    if not save_img(title_img_src,title_img_name,resharp=True):
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

    resp = requests.get('https://kenlu.net/category/news/',timeout=10)
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
        except Exception as e:
            print(e)
            pass
        time.sleep(60)