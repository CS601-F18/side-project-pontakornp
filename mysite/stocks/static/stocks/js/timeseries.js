/**
  use plotly.js library to create candlesticks graphs showing
  open price, high price, low price, and close price for each day
  from beginning of the year to most recent
**/
var trace1 = {
  type: "scatter",
  mode: "lines",
  name: 'AAPL High',
  x: x,
  y: high,
  line: {color: '#17BECF'}
}

var trace2 = {
  type: "scatter",
  mode: "lines",
  name: 'AAPL Low',
  x: x,
  y: low,
  line: {color: '#7F7F7F'}
}

var data = [trace1,trace2];

var layout = {
  title: 'Time Series Chart',
  xaxis: {
    autorange: true,
    range: [mindate, maxdate],
    rangeselector: {buttons: [
        {
          count: 1,
          label: '1m',
          step: 'month',
          stepmode: 'backward'
        },
        {
          count: 6,
          label: '6m',
          step: 'month',
          stepmode: 'backward'
        },
        {step: 'all'}
      ]},
    rangeslider: {range: [mindate, maxdate]},
    title: 'Date',
    type: 'date'
  },
  yaxis: {
    autorange: true,
    range: [minprice, maxprice],
    type: 'linear'
  }
};
Plotly.plot('timeseries-div', data, layout);