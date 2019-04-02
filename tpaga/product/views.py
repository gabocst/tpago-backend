from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer


class SaleListCreateAPIView(ListCreateAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer