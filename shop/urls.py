from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('new_item/', views.add_new_item, name='add_new_item'),
    path('new_category', views.add_new_cat, name='add_new_cat'),
    path('all_items/', views.show_all_items, name='show_all_items'),
    path('categories/', views.show_all_cats, name='show_all_cats'),
    path('categories/<int:cat_id>/', views.show_all_cats, name='show_all_cats'), 
]
