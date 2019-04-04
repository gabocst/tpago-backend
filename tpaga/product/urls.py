from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (SaleListAPIView, SaleRetrieveUpdateDestroyAPIView, paymentRequest, 
                    ProductListAPIView, paymentRequestConfirmation, confirmDelivery, refund, 
                    SaleProductListAPIView)


urlpatterns = format_suffix_patterns([
    url(r'^sale/create?/?$', paymentRequest, name='sale-create'),
    url(r'^sale?/?$', SaleListAPIView.as_view(), name='sale-list'),
	#url(r'^sale/(?P<pk>\d+)?/?$', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-update-retrieve-destroy'),
    
    url(r'^paymentConfirmation/(?P<token>[\w\-]+)?/?$', paymentRequestConfirmation, name='paymentConfirmation'),
    url(r'^confirmDelivery?/?$', confirmDelivery, name='confirmDelivery'),
    url(r'^refund?/?$', refund, name='refund'),

    url(r'^product?/?$', ProductListAPIView.as_view(), name='product-list'),
    url(r'^saleProduct?/?$', SaleProductListAPIView.as_view(), name='saleProduct-list'),
])
