"""ecommerce_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django import urls
from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotAllowed
from django.urls import path, include

from django.conf.urls.static import static # new
from django.conf import settings # new

from rest_framework import routers

router = routers.DefaultRouter()

from users_address import views
router.register(r'address', views.AddressViewSet)

from users import views
router.register(r'users', views.UsersViewSet)

def index(request):
    return HttpResponse('<h1>Forbidden!</h1>')

urlpatterns = [
    # path('', index),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include(router.urls)),
    path('api/', include('users_address.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('transaction.urls')),
    
    path('', include('product_category.urls')),
    path('', include('product_type.urls')),
    path('', include('product_subtype.urls')),
    path('', include('product_variant.urls')),
    path('', include('product_sku.urls')),
    path('', include('product_inventory.urls')),
    path('', include('unit_of_measure.urls')),
    path('', include('product.urls')),
    path('', include('cart.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)