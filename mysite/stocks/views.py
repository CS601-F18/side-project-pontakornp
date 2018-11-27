from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render
import json
from django.core import serializers
from .models import Stock, StockData

from iexfinance import get_historical_data
from datetime import datetime, date

from sqlalchemy import create_engine

import pandas as pd

# Create your views here.
def index(request):
	template = loader.get_template('stocks/index.html')
	return HttpResponse(template.render({}, request))

def extract_stock_data(request):
	start = datetime(2018, 1, 1)
	end = datetime.today()
	df = get_historical_data("ADBE", start=start, end=end, output_format='pandas')
	# print(df.head())
	# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	# 	print(df)

	template = loader.get_template('stocks/index.html')
	# engine = create_engine('mysql+mysqldb://root@localhost/stocks', echo=False)
	df.columns = ['open_price', 'high_price', 'low_price', 'close_price', 'volume']
	df['symbol'] = 'ADBE'
	df['stock_id'] = 2
	df['date'] = df.index
	print(df.to_dict('records'))
	StockData.objects.bulk_create(
	    StockData(**vals) for vals in df.to_dict('records')

	)
	# return HttpResponse(template.render(df.to_dict(), request))
	return HttpResponse("Hellooooo")

def show_dashboard(request):
	all_stocks = Stock.objects.all()
	if request.method == 'POST':
		print("yes")
		stock_id = request.POST.get('stock_id', -1)
		if (stock_id == -1):
			return JsonResponse({
				'status': 'false',
				'message': 'input_fail'
			}, 
			status=500
			)
			stock_data_qs = StockData.objects.filter(symbol='AAPL')
			stock_qs = Stock.objects.filter(symbol='AAPL')
		else:
			stock_data_qs = StockData.objects.filter(stock_id=stock_id)
			stock_qs = Stock.objects.filter(stock_id=stock_id)
	else:
		stock_qs = Stock.objects.order_by('stock_id').first()
		stock_data_qs = StockData.objects.filter(symbol=stock_qs.symbol)

	stock_json = serializers.serialize('json', stock_data_qs)
	context = {
		'all_stocks': all_stocks,
		'stock_qs': stock_qs,
		'stock_json': stock_json,
	}
	return render(request, 'stocks/index.html', context)
