from django.shortcuts import render, redirect
from django.views import View
from .models import Item
from .forms import ItemForm


def home(request):
    return render(request, 'inventory/home.html')


class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'inventory/item_list.html', {'items': items})


class ItemCreateView(View):
    def get(self, request):
        form = ItemForm()
        return render(request, 'inventory/item_form.html', {'form': form})

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'inventory/item_form.html', {'form': form})
