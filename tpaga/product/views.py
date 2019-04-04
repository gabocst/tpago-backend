from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
import json
import uuid
import requests
from requests.auth import HTTPBasicAuth
import os
from rest_framework import status
import datetime
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from utils.client import Client
from rest_framework.decorators import permission_classes, api_view



from .models import Product, Sale, SaleProduct
from .serializers import ProductSerializer, SaleListSerializer, SaleSerializer, SaleProductListSerializer


class SaleListAPIView(ListAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleListSerializer
	permission_classes = [AllowAny]


class ProductListAPIView(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]


class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer
	permission_classes = [AllowAny]


class SaleProductListAPIView(ListAPIView):
	queryset = SaleProduct.objects.all()
	serializer_class = SaleProductListSerializer
	permission_classes = [IsAuthenticated]


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
def paymentRequest(request):
	
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		product = Product.objects.get(id=body['product']['id'])
		client = Client()

		total = body['quantity'] * body['product']['cost']
		
		sale = Sale(
			total=total,
			terminal_id=body['terminal_id'],
			purchase_description=body['purchase_description'],
			token=None,
			status=None,
			user_ip_address=body['user_ip_address']
		)
		sale.save()

		r = client.create_payment_request(
			total,
			'https://example.com/compra/348820', #link finalizacion de compra (gracias por su compra)
			None,
			sale.pk,  
			body['terminal_id'],
			body['purchase_description'],
			body['user_ip_address'],
		)
		response = json.loads(r)

		sale.token = response["token"]
		sale.status = response["status"]
		sale.save()

		saleProduct = SaleProduct(
			sale=sale,
			product=product,
			cost=body['product']['cost'],
			quantity=body['quantity']
		)
		saleProduct.save()
		
	except Exception as ex:
		error = {'{}'.format(_('detail')): ",".join(ex.args) if ex.args else '{}'.format(_('Unknown Error'))}		
		return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response(response, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def paymentRequestConfirmation(request, token):
	
	client = Client()
	r = client.payment_request_confirmation(
		token,
	)
	response = json.loads(r)

	sale = Sale.objects.filter(token=token).update(status=response["status"])

	return Response(response, status=status.HTTP_200_OK)#ver si retornar lo de tpaga o lo mio


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
def confirmDelivery(request):
	
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		client = Client()
		r = client.confirm_delivery(
			body['token'],
		)
		response = json.loads(r)
		sale = Sale.objects.filter(token=body['token']).update(status=response["status"])
		
	except Exception as ex:
		error = {'{}'.format(_('detail')): ",".join(ex.args) if ex.args else '{}'.format(_('Unknown Error'))}		
		return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response(response, status=status.HTTP_200_OK)#ver si retornar lo de tpaga o lo mio


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def refund(request):
	
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		client = Client()

		r = client.refund_payment(
			body['token'],
		)
		response = json.loads(r)
		
		sale = Sale.objects.filter(token=body['token']).update(status=response["status"])
		
	except Exception as ex:
		error = {'{}'.format(_('detail')): ",".join(ex.args) if ex.args else '{}'.format(_('Unknown Error'))}		
		return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response(response, status=status.HTTP_200_OK)