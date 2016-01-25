import networkx as nx 
import matplotlib.pyplot as plt
graph = nx.Graph()

graph.add_nodes_from(range(10))
graph.add_edge(1, 2)
graph[1][2]['weight'] =1

nx.draw(graph)
plt.show()