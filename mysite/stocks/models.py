from django.db import models

# Create your models here.
class Stock(models.Model):
	stock_id = models.AutoField(db_column='stock_id', primary_key=True)
	symbol = models.CharField(max_length=4, unique=True)
	company_name = models.CharField(max_length=50)

	class Meta:
		db_table = 'stocks'

class StockData(models.Model):
	stock_data_id = models.AutoField(db_column='stock_data_id', primary_key=True)
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	symbol = models.CharField(max_length=4)
	open_price = models.DecimalField(max_digits=10, decimal_places=2)
	close_price = models.DecimalField(max_digits=10, decimal_places=2)
	high_price = models.DecimalField(max_digits=10, decimal_places=2)
	low_price = models.DecimalField(max_digits=10, decimal_places=2)
	volume = models.IntegerField(default=0)
	date = models.DateField()
	create_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'stock_data'
		unique_together = (('stock', 'date'),)