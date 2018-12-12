from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
import json
from django.core import serializers
from .models import Stock, StockData

from iexfinance import get_historical_data
from datetime import date
import datetime
import pandas as pd

# show dashboard with stock data in times series and candle sticks graphs
def show_dashboard(request):
	all_stocks = Stock.objects.all()
	if request.method == 'GET':
		stock_id = request.GET.get('stock_id', -1)
		if stock_id == -1:
			stock_qs = Stock.objects.order_by('stock_id').first()
			stock_data_qs = StockData.objects.filter(symbol=stock_qs.symbol)
		else:
			stock_qs = Stock.objects.filter(stock_id=stock_id)[0]
			stock_data_qs = StockData.objects.filter(stock_id=stock_id)
	else:
		return HttpResponseNotAllowed("Please try again with GET request")
	stock_json = serializers.serialize('json', stock_data_qs)
	context = {
		'all_stocks': all_stocks,
		'stock_qs': stock_qs,
		'stock_json': stock_json,
		'stock_id': stock_id,
	}
	return render(request, 'stocks/index.html', context)

# for extracting stock data open price, high price, low price, and close price 
# from iexfinance library
def extract_stock_data(request):
	stocks = Stock.objects.all()
	end = date.today()
	count = 0
	for stock in stocks:
		stock_id = stock.stock_id
		symbol = stock.symbol
		last_date_row = StockData.objects.filter(symbol=symbol).order_by('-date')[0]
		last_date = last_date_row.date
		start = last_date + datetime.timedelta(days=1)
		if(start < end):
			df = get_historical_data(symbol, start=start, end=end, output_format='pandas')
			template = loader.get_template('stocks/index.html')
			df.columns = ['open_price', 'high_price', 'low_price', 'close_price', 'volume']
			df['stock_id'] = stock_id
			df['symbol'] = symbol
			df['date'] = df.index
			StockData.objects.bulk_create(
			    StockData(**vals) for vals in df.to_dict('records')
			)
			count += 1
	if count > 0:
		return HttpResponse("Done Extracting Data")
	else:
		return HttpResponse("You have the most recent data, no data to be extracted")
