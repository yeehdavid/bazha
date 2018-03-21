from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Shoes
import markdown
from Order.forms import OrderForm

# Create your views here.

def detail(request, pk):
    shoes = get_object_or_404(Shoes, pk=pk)
    form = OrderForm()
    return render(request, 'Shoes/detail.html', context={'tea': shoes, 'form':form})