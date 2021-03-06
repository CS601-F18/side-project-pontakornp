/**
  use plotly.js library to create candlesticks graphs showing
  open price, high price, low price, and close price for each day
  from beginning of the year to most recent
**/
var trace1 = {
  x: x,
  
  close: close,
  
  decreasing: {line: {color: '#7F7F7F'}}, 
  
  high: high,
  
  increasing: {line: {color: '#17BECF'}}, 
  
  line: {color: 'rgba(31,119,180,1)'}, 
  
  low: low,
  
  open: open,
  type: 'candlestick', 
  xaxis: 'x', 
  yaxis: 'y'
};

var data = [trace1];

var layout = {
  title: 'Candlestick Chart',
  dragmode: 'zoom', 
  margin: {
    r: 10, 
    t: 25, 
    b: 40, 
    l: 60
  }, 
  showlegend: false, 
  xaxis: {
    autorange: true, 
    domain: [0, 1], 
    range: [mindate, maxdate], 
    rangeslider: {range: [mindate, maxdate]}, 
    title: 'Date', 
    type: 'date',
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
  }, 
  yaxis: {
    autorange: true, 
    domain: [0, 1], 
    range: [minprice, maxprice], 
    type: 'linear'
  }
};

Plotly.plot('plotly-div', data, layout);