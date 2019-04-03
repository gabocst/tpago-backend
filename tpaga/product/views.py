from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
import json
import uuid
import requests
from requests.auth import HTTPBasicAuth
import os
import datetime
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from utils.client import Client
from rest_framework.decorators import permission_classes, api_view



from .models import Product, Sale
from .serializers import ProductSerializer, SaleListSerializer, SaleSerializer


class SaleCreateAPIView(CreateAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer
	permission_classes = [AllowAny]


class SaleListAPIView(ListAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleListSerializer
	permission_classes = [AllowAny]


class SaleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer
	permission_classes = [AllowAny]


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
def createSale(request):
	
	try:
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		print(body)
		product = Product.objects.get(id=body['product'])
		print(product["cost"])
		client = Client()

		r = client.create_payment_request(
			body['cost'],
			'https://example.com/compra/348820',
			'https://example.com/comprobante/348820',
			body['cost'],  #order_id luego de ingresar en bd
			body['terminal_id'],
			body['purchase_description'],
			body['user_ip_address'],
		)

		print(json.loads(r))
		#response = json.loads(r)
		#res = json.dumps(response, indent=4, sort_keys=True)
		#print(res)

		



	except Exception as ex:
		#error = {'{}'.format(_("strings.detail")): ",".join(ex.args) if ex.args else '{}'.format(_("strings.unknown_error"))}
		return Response(ex, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

	return Response("serializer.data", status=status.HTTP_201_CREATED)







# @csrf_exempt
# @api_view(['POST'])
# @permission_classes((AllowAny, ))
# def createSale(request):
	
# 	try:
# 		body_unicode = request.body.decode('utf-8')
# 		body = json.loads(body_unicode)

# 		#dateStart = timezone.now()

# 		#crear json

# 		#hacer la llamada post desde aqui
# 		trade = Trade.objects.create(
# 			user=request.user,
# 			dateStart=dateStart,
# 			description=body['trade']['description'],
# 			tradeType=body['trade']['tradeType'],
# 			minAmount=body['trade']['minAmount'],
# 			maxAmount=body['trade']['maxAmount'],
# 			limitToFiatAmount=body['trade']['limitToFiatAmount'],
# 			currency=Currency.objects.get(id=body['trade']['currency']),
# 			price=body['trade']['price'])


# 	except Exception as ex:
# 		error = {'{}'.format(_(strings.detail)): ",".join(ex.args) if ex.args else '{}'.format(_(strings.unknown_error))}
# 		return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 	return Response(serializer.data, status=status.HTTP_201_CREATED)