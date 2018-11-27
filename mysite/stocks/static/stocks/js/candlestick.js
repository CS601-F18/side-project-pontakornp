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
    type: 'date'
  }, 
  yaxis: {
    autorange: true, 
    domain: [0, 1], 
    range: [minprice, maxprice], 
    type: 'linear'
  }
};

Plotly.plot('plotly-div', data, layout);