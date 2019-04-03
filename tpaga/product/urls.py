from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (SaleCreateAPIView, SaleListAPIView, SaleRetrieveUpdateDestroyAPIView, createSale)


urlpatterns = format_suffix_patterns([
    url(r'^sale/create?/?$', SaleCreateAPIView.as_view(), name='sale-create'),
    url(r'^sale?/?$', SaleListAPIView.as_view(), name='sale-list'),
	url(r'^sale/(?P<pk>\d+)?/?$', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-update-retrieve-destroy'),
    

    url(r'^sale/create2?/?$', createSale, name='sale-create-2'),	
])
