NASDAQ Tech Companies Stocks Web Application
============================================

## Specifications

1. Scrape specific fields of 20 tech companies stock information starting from January 1 2018 to most recent available data.
2. Create a database to store those data scraped.
3. Develop a web application to display stocks open, high, low, close price over time in 2 different charts and allow user to filter date range and sort by volume of day, month, or year.

## Technologies Use

- Extract data - iexfinance (Python library) https://pypi.org/project/iexfinance/
- Develop web application - Python/Django
- Display front-end interfaces - HTML, CSS, JavaScript/JQuery, plotly.js https://plot.ly/javascript/candlestick-charts/
- Manage database - SQL/MySQL
- Source code management tool - Git

## Stock Picked

- Apple Inc. (AAPL)
- Adobe Inc. (ADBE)
- Amazon.com, Inc. (AMZN)
- Baidu, Inc. (BIDU)
- Salesforce.com Inc (CRM)
- Cisco Systems, Inc. (CSCO)
- Dell Technologies Inc. (DVMT)
- Facebook Inc. (FB)
- Alphabet Inc. (GOOGL)
- Alphabet Inc. (GOOG)
- International Business Machines Corporation (IBM)
- Microsoft Corporation (MSFT)
- Netflix, Inc. (NFLX)
- Oracle Corporation (ORCL)
- Red Hat, Inc. (RHT)
- SAP SE (SAP)
- Square, Inc. (SQ)
- Tesla, Inc (TSLA)
- Twitter, Inc. (TWTR)
- Workday, Inc. (WDAY)

## Stock Data to be Extracted

1. Open Price
2. Open Date
3. Close Price
4. Close Date
5. High Price
6. Low Price
7. Volume

## Sample Chart

1. Candlestick chart - showing open, high, low, close price for a period
![candlestick](https://plot.ly/~RPlotBot/4305/basic-candlestick-chart.png)

Source: https://plot.ly/javascript/candlestick-charts/

2. Time Series chart - showing high, low price for a period
![timeseries](https://plot.ly/~priyatharsan/18/time-series-with-rangeslider.png)

Source: https://plot.ly/javascript/time-series/

## Features

- Filter date range for each graph
- Sort stock by volume of day, month, or year
