import json
from pprint import pprint
from networkx.readwrite import json_graph
import networkx

def create_party_graph(congress):

    
    file_name = 'gov_data/static/gov_data/'+str(congress)+'_force.json'
    json_data=open(file_name).read()
    data = json.loads(json_data)
    
    graph = json_graph.node_link_graph(data)
    republican_graph = json_graph.node_link_graph(data)
    democrat_graph = json_graph.node_link_graph(data)

    party=networkx.get_node_attributes(graph,'party')
    
    republican_list = []
    democrat_list = []
    other_list = []
    for node in graph.nodes():
        try:
            if party[node] == 'r':
                republican_list.append(node)
            elif party[node] == 'd':
                democrat_list.append(node)
            else:
                other_list.append(node)
        except:
            other_list.append(node)

    republican_graph.remove_nodes_from(democrat_list)
    republican_graph.remove_nodes_from(other_list)

    democrat_graph.remove_nodes_from(republican_list)
    democrat_graph.remove_nodes_from(other_list)

    republican_data = json_graph.node_link_data(republican_graph)
    democrat_data = json_graph.node_link_data(democrat_graph)

    
    json.dump(republican_data, open('gov_data/static/gov_data/'+ str(congress) + '_rep_force.json','w'))
    json.dump(democrat_data, open('gov_data/static/gov_data/'+ str(congress) + '_dem_force.json','w'))

for congress in range(92, 114):
    create_party_graph(congress)
    print(congress)

