from django.apps import AppConfig
from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=50)
	cost = models.FloatField()


	class Meta:
		db_table = "product"
	
	def __str__(self):
		return '{}'.format(self.name)


class Sale(models.Model):
	total = models.FloatField()
	terminal_id = models.CharField(max_length=50, null=False)
	purchase_description = models.CharField(max_length=255, null=True)
	purchase_items = models.CharField(max_length=1000, null=True)
	token = models.CharField(max_length=100, null=True)
	status = models.CharField(max_length=20, null=True)
	user_ip_address = models.CharField(max_length=20, null=True)

	class Meta:
		db_table = "sale"


class SaleProduct(models.Model):
	sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
	product = models.ForeignKey('Product', on_delete=models.CASCADE)
	cost = models.FloatField()
	quantity = models.PositiveIntegerField()

	class Meta:
		db_table = "saleProduct"
	
	def set_amount(self):
		return self.cost * self.quantity
	
	amount = property(set_amount)