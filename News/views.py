from django.shortcuts import render
from .models import Article, Article_Part
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def detail(request, pk):
    a = get_object_or_404(Article, pk=pk)
    a_p = Article_Part.objects.filter(belong_to=a)
    return render(request, 'News/detail.html', context={'a': a,'a_p':a_p})

