from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from News.models import Article
from Shoes.models import Shoes, Brand

def index(request):
    all_articles = Article.objects.all().order_by('-created_time')

    article_list = all_articles[3:]
    first_one = None
    second_one = None
    third_one = None

    paginator = Paginator(article_list, 12)  # 实例化一个分页对象

    page = request.GET.get('page')  # 获取页码
    if page == '1':
        first_one = all_articles[0]
        second_one = all_articles[1]
        third_one = all_articles[2]

    try:
        article_list = paginator.page(page)  # 获取某页对应的记录

    except PageNotAnInteger:  # 如果页码不是个整数
        try:
            first_one = all_articles[0]
            second_one = all_articles[1]
            third_one = all_articles[2]
        except:
            pass
        article_list = paginator.page(1)  # 取第一页的记录

    except EmptyPage:  # 如果页码太大，没有相应的记录
        article_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render(request, 'index.html', context={'article_list': article_list, 'index_active': 'active',
                                                  'first_one':first_one,'second_one':second_one,
                                                  'third_one': third_one})


def nike(request):
    nike_brand = Brand.objects.filter(name = '耐克')
    shoes = Shoes.objects.filter(brand = nike_brand)
    return  render(request, 'brand_index.html', context={'shoes':shoes, 'nike_active': 'active'})

def adidas(request):
    nike_brand = Brand.objects.filter(name = '阿迪达斯')
    shoes = Shoes.objects.filter(brand = nike_brand)
    return  render(request, 'brand_index.html', context={'shoes':shoes, 'adidas_active': 'active'})

def nb(request):
    nike_brand = Brand.objects.filter(name = '新百伦')
    shoes = Shoes.objects.filter(brand = nike_brand)
    return  render(request, 'brand_index.html', context={'shoes':shoes, 'nb_active': 'active'})

def asics(request):
    nike_brand = Brand.objects.filter(name = '亚瑟士')
    shoes = Shoes.objects.filter(brand = nike_brand)
    return  render(request, 'brand_index.html', context={'shoes':shoes, 'asics_active': 'active'})

def others(request):
    nike_brand = Brand.objects.filter(name = '其他')
    shoes = Shoes.objects.filter(brand = nike_brand)
    return  render(request, 'brand_index.html', context={'shoes':shoes, 'others_active': 'active'})
# Create your views here.
