from rest_framework import serializers

from product.models import Product, Sale


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ("__all__")


class SaleSerializer(serializers.ModelSerializer):
	product = ProductSerializer(read_only=True)

	class Meta:
		model = Sale
		fields = ("id", "total", "terminal_id", "purchase_description", "purchase_items", "user_ip_address")


class SaleListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sale
		fields = ("__all__")