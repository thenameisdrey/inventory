from django.shortcuts import render, redirect
from .models import NewStock, StockDetails
from .forms import NewStockForm, StockDetailsForm
from django.views.decorators.http import require_POST
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'vetsark/index.html')

def stock(request):
    stock = StockDetails.objects.all()
    context = {'stock': stock}

    return render(request, 'vetsark/stock.html', context)

def add_stock(request):
    new_stock = NewStock.objects.all()
    form = StockDetailsForm(request.POST)
    
    if form.is_valid():
        new_add = NewStock(name=request.POST['name'])
        new_add.save()

    context = {'new_stock': new_stock, 'form': form}

    return render(request, 'vetsark/add_new_stock.html', context)












def add_category(request):
    category = NewStock.objects.all()
    new_form = NewStockForm(request.POST)

    if new_form.is_valid():
        new_cat = NewStock(name=request.POST['name'])
        new_cat.save()

    context = { 'category': category, 'form': new_form}
    return render(request, 'vetsark/new_category.html', context)

# @require_POST
# def new_category(request):
#     new_form = NewStockForm(request.POST)
    
#     if new_form.is_valid():
#         new_cat = NewStock(name=request.POST['name'])
#         new_cat.save()

#         return redirect('addstock')

