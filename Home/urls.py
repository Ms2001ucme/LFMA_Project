from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.index, name='home'),
    path("about/",views.about, name='about'),
    path("services/",views.services, name='services'),
    path("contact/",views.contact, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path('productform/',views.my_view, name='productform'),
    path('product/<str:slug>/',views.ProductDynamicView, name='productview'),
    path('order/<int:id>/',views.OrderDynamicView, name='orderview'),
    path('product/<str:slug>/buy/',views.order_product, name='orderproduct'),
    path('ordersplacedlist/',views.OrdersView, name='orderplacedlist'),
     path('orderrecivedlist/',views.OrdersRecievedView, name='orderrecivedlist'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)