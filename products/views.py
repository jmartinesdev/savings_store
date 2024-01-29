from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/products_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).          get_context_data(*args, **kwargs)
        print(context)
        return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/products_list.html", context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
def ProductDetailView(request)
    query_set = Product.objects.all()
    context = {
        'object_list': query_set
    }
    return render(request, "products/detail.html", context)