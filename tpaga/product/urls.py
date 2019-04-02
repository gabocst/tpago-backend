from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (SaleListCreateAPIView, SaleRetrieveUpdateDestroyAPIView)


urlpatterns = format_suffix_patterns([
    url(r'^sale?/?$', SaleListCreateAPIView.as_view(), name='sale-list-create'),
	url(r'^sale/(?P<pk>\d+)?/?$', SaleRetrieveUpdateDestroyAPIView.as_view(), name='sale-update-retrieve-destroy'),
    
])
