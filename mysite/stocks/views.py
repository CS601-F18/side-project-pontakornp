from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Stock, StockData

from iexfinance import get_historical_data
from datetime import datetime, date

from sqlalchemy import create_engine

import pandas as pd

# Create your views here.
def index(request):
	template = loader.get_template('stocks/index.html')
	return HttpResponse(template.render({}, request))

def getStock(request):
	start = datetime(2018, 1, 1)
	end = datetime(2018, 11, 21)
	df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
	# print(df.head())
	# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	# 	print(df)

	template = loader.get_template('stocks/index.html')
	# engine = create_engine('mysql+mysqldb://root@localhost/stocks', echo=False)
	df.columns = ['open_price', 'high_price', 'low_price', 'close_price', 'volume']
	df['symbol'] = 'AAPL'
	df['stock_id'] = 1
	df['date'] = df.index
	print(df.to_dict('records'))
	StockData.objects.bulk_create(
	    StockData(**vals) for vals in df.to_dict('records')

	)
	return HttpResponse("Hellooooo")
	# return HttpResponse(template.render(df.to_dict(), request))