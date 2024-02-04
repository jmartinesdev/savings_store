from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view, ProductFeaturedListView, ProductFeaturedDetailView
from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
    path('register/', register_page),
	path('home/', home_page, name='home'),
	path('about/', about_page),
	path('contact/', contact_page),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_page),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
	path('admin/', admin.site.urls),
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products-fbv/<int:pk>', product_detail_view)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)