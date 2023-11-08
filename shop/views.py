from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Goods
from .models import *
from .forms import *


# Create your views here.
def main_page(request):
    return render(request, 'shop/main.html', context={'title:': 'Головна'})


def add_new_item(request):
    
    def save_item(f:object):
        name = f['name']
        category = f['category']
        weight = f['weight']
        price = f['price']
        good = Goods(name=name, category=category, weight=weight, price=price)
        good.save()
        print('New Goods SAVED')


    if request.method == 'POST':
        form = AddGood(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            save_item(f)
            print('  Валідована форма:', f)
            
        else:
            print('  НE валідована форма:', form.cleaned_data)
    else:
        form = AddGood()

    context = {
        'form': form,
        'title': 'Новий товар',
    }
    return render(request, 'shop/add_good.html', context=context)


def add_new_cat(request):

    def save_cat(f:object):
        name = f['name']
        have_limit = f['have_limit']
        cat = Category(name=name, have_limit=have_limit)
        cat.save()
        print('New Category SAVED')


    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            print('  Валідована форма:', f)
            save_cat(f)
        else:
            print('  НE валідована форма:', form.cleaned_data)
    else:
        form = AddCategory()

    context = {
        'form': form,
        'title': 'Нова категорія',
    }
    return render(request, 'shop/add_cat.html', context=context)


def show_all_items(request):
    all_goods = Goods.objects.all().values()
    context = {
        'goods': all_goods,
        'title': 'Товари',
    }
    return render(request, 'shop/goods.html', context=context)
    # return HttpResponse('SHOW ALL ITEMS PAGE')


def show_all_cats(request):
    all_cats = Category.objects.all().values()
    context = {
        'cats': all_cats,
        'title': 'Категорії',
    }
    return render(request, 'shop/all_cats.html', context=context)


# def show_cat_goods(request, cat_id):
#     goods = Goods.objects.filter(category=cat_id)
#     context = {
#         'goods': goods,
#     }
#     return render(request, 'shop/all_cats.html', context=context)




