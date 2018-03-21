import requests
import image
from PIL import Image
from bs4 import BeautifulSoup
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'bazha.settings'
django.setup()

import requests
from crawler.langconv import *
import time
from bs4 import BeautifulSoup
from News.models import Article, Article_Part


url = 'https://kenlu.net/wp-content/uploads/2018/03/reebok-sign-gal-gadot-1-750x430.jpg'

ir = requests.get(url)
if ir.status_code == 200:
    open('../Main/static/Main/img/test.jpg', 'wb').write(ir.content)

A = Article(title = 'title', title_img = 'title_img')
A.save()
print(A.pk)
A_P = Article_Part(img='News/test.jpg', belong_to=A, order=0)
A_P.save()