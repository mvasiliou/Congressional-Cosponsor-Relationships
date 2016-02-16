$(document).ready(function(){

  var width = 1140,
      height = 625;
  
  var color = d3.scale.ordinal()
      .domain(['r', 'd', 'o'])
      .range(['#FF563B','#29859F','#FF9E3B']);
  
  var force = d3.layout.force()
      .charge(-300)
      .linkDistance(function(d){ return (d.weight) + (Math.log((1 / d.weight)) * -50); })
      .size([width, height]);
  
  //Creates box to plot in based on width and height
  var svg = d3.select("div #box").append("svg:svg")
      .attr("width", width)
      .attr("height", height)
  
    svg.append('rect')
      .attr('width', width)
      .attr('height', height)
      .style('fill', 'none')
      .style('stroke', '#000')
      .style('stroke-width', 10);
  
  function add_nodes_and_edges(file_name) {
      svg.selectAll('.node')
          .remove()
      svg.selectAll('.link')
          .remove()

    d3.json(file_name, function(error, graph) {
      if (error) throw error;

      force
          .nodes(graph.nodes)
          .links(graph.links)
          .start();
    
      var link = svg.selectAll(".link")
          .data(graph.links)
          .enter().append("line")
          .attr("class", "link")
          .style("stroke-width", function(d) { return d.weight / 2; });
    
      link.append("title")
          .text(function(d) {return d.weight})     
      var node = svg.selectAll(".node")
          .data(graph.nodes)
          .enter().append("circle")
          .attr("class", "node")
          .on('dblclick', function(d, i) {
            url = 'senators/' + d.id + '/';
            window.location.href = url;
          })
          .attr("r", function(d){ return d.size / 15})
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
  }
  
  add_nodes_and_edges('/static/gov_data/force.json');

  $("body").on("click", "#senate", (function () {
    add_nodes_and_edges('/static/gov_data/force.json')
  }));

  $("body").on("click", "#democrat", (function () {
    add_nodes_and_edges('/static/gov_data/democrat_force.json')
  }));  

  $("body").on("click", "#republican", (function () {
    add_nodes_and_edges('/static/gov_data/republican_force.json')
  }));

  $("body").on("click", "#edge_1", (function () {
    add_nodes_and_edges('/static/gov_data/one_force.json')
  }));

  $("body").on("click", "#edge_5", (function () {
    add_nodes_and_edges('/static/gov_data/five_force.json')
  }));

  $("body").on("click", "#edge_10", (function () {
    add_nodes_and_edges('/static/gov_data/ten_force.json')
  }));
});