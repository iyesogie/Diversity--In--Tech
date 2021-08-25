var keys=["KNN","GridSearchCV","Sequential"]
var values=[0.714,0.783,0.857]
// create trace variable for the plot
var trace1 = {
    x: keys,
    y: values,
    type:"bar",
};
// create data variable
var data = [trace1];
var layout = {
  height:450,
  xaxis: {
    automargin: true,
  },
  yaxis:{
    title:"Accuray Score of Test Samples",},
}
// create the bar plot
Plotly.newPlot("bar-chart", data, layout);