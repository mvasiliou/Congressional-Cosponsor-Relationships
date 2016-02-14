var width = 1200,
    height = 700;

var color = d3.scale.ordinal()
    .domain(['r', 'd', 'o'])
    .range(['#FF563B','#29859F','#FF9E3B']);

var force = d3.layout.force()
    .charge(-1000)
    .linkDistance(100)
    .size([width, height]);


//Creates box to plot in based on width and height
var svg = d3.select("body").append("svg:svg")
    .attr("width", width)
    .attr("height", height)
    .append('svg:g')
    .attr("transform", "translate(" + width / 4 + "," + height / 3 + ")");

svg.append('svg:rect')
  .attr('width', width)
  .attr('height', height)
  .style('stroke', '#000');

d3.json('/static/gov_data/force.json', function(error, graph) {
  if (error) throw error;

  force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();

  var link = svg.selectAll(".link")
      .data(graph.links)
      .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("class", "node")
      .on('click', function(d, i) {
        url = 'senators/' + d.id + '/';
        window.location.href = url;
      })
      .attr("r", function(d){ return d.size / 10})
      .style("fill", function(d) { return color(d.party); })
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.label; });

  force.on("tick", function() {
    node.attr("cx", function(d) { return d.x = Math.max(15, Math.min(width - 15, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(15, Math.min(height - 15, d.y)); });

    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });    
  });
});