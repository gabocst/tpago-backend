from rest_framework import serializers

from product.models import Product, Sale


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ("__all__")


class SaleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sale
		fields = ("id", "amount", "terminal_id", "purchase_description", "purchase_items", "user_ip_address", "product")


class SaleListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sale
		fields = ("__all__")