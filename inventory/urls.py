from django.urls import path
from .views import ItemListView, ItemCreateView, home

urlpatterns = [
    path('', home, name='home'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/new/', ItemCreateView.as_view(), name='item_create'),
]
