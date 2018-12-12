from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
import json
from django.core import serializers
from .models import Stock, StockData

from iexfinance import get_historical_data
from datetime import datetime, date

import pandas as pd

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
		return HttpResponse("Please try again with GET request")

	stock_json = serializers.serialize('json', stock_data_qs)
	context = {
		'all_stocks': all_stocks,
		'stock_qs': stock_qs,
		'stock_json': stock_json,
		'stock_id': stock_id,
	}
	return render(request, 'stocks/index.html', context)

def extract_stock_data(request):
	start = datetime(2018, 11, 22)
	end = datetime.today()
	df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
	template = loader.get_template('stocks/index.html')
	df.columns = ['open_price', 'high_price', 'low_price', 'close_price', 'volume']
	df['symbol'] = 'AAPL'
	df['stock_id'] = 1
	df['date'] = df.index
	print(df.to_dict('records'))
	StockData.objects.bulk_create(
	    StockData(**vals) for vals in df.to_dict('records')
	)
	return HttpResponse("Done Extracting Data")
