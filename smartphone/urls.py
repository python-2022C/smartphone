"""smartphone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from smartphone_app.views import (
    get_products,
    get_product,
    add_product,
    update_product,
    delete_product,
    get_products_by_company,
    get_products_by_color,
    get_products_by_memory_range,
    get_products_by_RAM,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', get_products),
    path('product/<int:id>', get_product),  # <int:id> is a variable
    path('add_product/', add_product),
    path('update_product/<int:id>', update_product),
    path('delete_product/<int:id>', delete_product),
    path('products/color/<str:color>', get_products_by_color),
    path('products/<str:memory>', get_products_by_memory_range),
    path('products_RAM/<str:RAM>', get_products_by_RAM),
]
    path('products/RAM/<str:RAM>', get_products_by_RAM),
    path('products/company/<str:company>', get_products_by_company),
    path('products/memory/<str:memory>', get_products_by_memory_range)
]
