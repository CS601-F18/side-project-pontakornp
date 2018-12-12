/** 
  initializes necessary variables for setting up graphs
  parse json data to javascrip variables
**/
var data = JSON.parse(stock_json);
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