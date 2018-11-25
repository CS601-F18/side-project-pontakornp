var x = [];
var close = [];
var high = [];
var low = [];
var open = [];
for (var i = 0; i < data.length; i++){
    x.push(new Date(data[i].fields.date));
    open.push(data[i].fields.open_price);
    close.push(data[i].fields.close_price);
    high.push(data[i].fields.high_price);
    low.push(data[i].fields.low_price);
}

var maxdate = new Date(Math.max.apply(null, x));
var mindate = new Date(Math.min.apply(null, x));
var maxprice = Math.max.apply(null, low);
var minprice = Math.min.apply(null, high);
console.log(maxdate);
console.log(mindate);
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