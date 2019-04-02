from django.apps import AppConfig
from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=50, null=True)


	class Meta:
		db_table = "product"


class Sale(models.Model):
	amount = models.PositiveIntegerField(default=0, null=False)
	cost = models.FloatField(default=0)
	terminal_id = models.CharField(max_length=50, null=False)
	purchase_description = models.CharField(max_length=255, null=True)
	purchase_items = models.CharField(max_length=1000, null=True)
	token = models.CharField(max_length=100, null=True)
	status = models.CharField(max_length=20, null=True)
	user_ip_address = models.CharField(max_length=20, null=True)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)


	class Meta:
		db_table = "sale"