/* implementation heavily influenced by http://bl.ocks.org/1166403 */
            
// define dimensions of graph; pretty much arbitrary/style decision
var m = [80, 80, 80, 80]; // margins
var w = 800 - m[1] - m[3]; // width
var h = 400 - m[0] - m[2]; // height
        
// data and x_axis_labels arrays (lists)
var data = {{score_list}};
var x_axis_labels = {{congress_list}}//[95, 96, 97, 98, 99]

// sets boundaries of the graph
var x = d3.scale.linear().domain([x_axis_labels[0], x_axis_labels[x_axis_labels.length - 1] ]).range([0, w]);
var y = d3.scale.linear().domain([0, 2000]).range([h, 0]);


// create a line function that can convert data and labels into x and y points
var line = d3.svg.line()

    .x(function(d,i) { return x(x_axis_labels[i]); })
    .y(function(d) { return y(d); })

    // Add an SVG element with the desired dimensions and margin.
    var graph = d3.select("#graph").append("svg:svg")
          .attr("width", w + m[1] + m[3])
          .attr("height", h + m[0] + m[2])
        // .append("svg:g") Is this a necessary line? 
          .attr("transform", "translate(" + m[3] + "," + m[0] + ")");

    // makes the x-axis
    var xAxis = d3.svg.axis().scale(x).ticks(x_axis_labels.length);
    graph.append("svg:g")
          .attr("class", "x axis")
          .attr("transform", "translate(70," + h + ")")
          .call(xAxis);

    // makes the y-axis
    var yAxisLeft = d3.svg.axis().scale(y).orient("left");
    graph.append("svg:g")
          .attr("class", "y axis")
          .attr("transform", "translate(70,0)")
          .call(yAxisLeft);

    graph.append("svg:path").attr("d", line(data));