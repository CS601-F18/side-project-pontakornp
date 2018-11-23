from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from iexfinance import get_historical_data
from datetime import datetime

import pandas as pd

# Create your views here.
def index(request):
	template = loader.get_template('stocks/index.html')
	return HttpResponse(template.render({}, request))

def home(request):
	start = datetime(2018, 11, 1)
	end = datetime(2018, 11, 22)
	df = get_historical_data("AAPL", start=start, end=end, output_format='pandas')
	# print(df.head())
	with pd.option_context('display.max_rows', None, 'display.max_columns', None):
		print(df)
	return HttpResponse("Hello")