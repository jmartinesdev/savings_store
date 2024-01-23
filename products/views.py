from django.views.generic import ListView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'qs' : queryset
    }
    return render(request, "products/list.html", context)