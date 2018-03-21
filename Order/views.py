from django.shortcuts import render, get_object_or_404, redirect
from Shoes.models import Shoes
from .models import Buyer
from .forms import OrderForm

def post_order(request, order_pk):
    shoes = get_object_or_404(Shoes, pk=order_pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.shoes = shoes
            order.save()
            return render(request, 'buy_success.html')
        else:
            return redirect(shoes)
    return redirect(shoes)

# Create your views here.
