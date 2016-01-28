import json
from pprint import pprint
import urllib.request
import networkx as nx
import matplotlib.pyplot as plt

def create_rep_weights():
    rep_dict = {}
    get_rep_codes(rep_dict)
    
    for rep in rep_dict:
        get_rep_weight(rep, rep_dict)
    return rep_dict    

def make_url_request(url):
    response = urllib.request.urlopen(url)
    str_response = response.read().decode('utf-8')
    data = json.loads(str_response)
    return data

def get_rep_codes(rep_dict):
    url = "https://www.govtrack.us/api/v2/role?current__exact=true&&role_type__exact=senator"
    data = make_url_request(url)
    for senator in data['objects']:
        s_id = senator['person']['id']
        if s_id not in rep_dict:
            rep_dict[s_id] = {}

def get_rep_weight(rep, rep_dict):
    rep_dict[rep]['in_dict'] = {}
    rep_dict[rep]['total'] = 0

    bills_sponsored_list = find_sponsored_bills(rep)
    for bill in bills_sponsored_list:
        url = 'https://www.govtrack.us/api/v2/cosponsorship?bill__exact=' + str(bill)
        data = make_url_request(url)
        num_cosponsors = data['meta']['total_count']
        rep_dict[rep]['total'] += num_cosponsors
        for person in data['objects']:
            cosponsor = person['person']
            if cosponsor not in rep_dict[rep]['in_dict']:
                rep_dict[rep]['in_dict'][cosponsor] = 0
            rep_dict[rep]['in_dict'][cosponsor] += 1

def find_sponsored_bills(rep):
    url = "https://www.govtrack.us/api/v2/bill?limit=6000&&introduced_date__gt=2015-01-01&&sponsor__exact=" + str(rep)
    data = make_url_request(url)
    count = data['meta']['total_count']
    sponsored_bills = []
    for bill in data['objects']:
        sponsored_bills.append(bill['id'])
    return sponsored_bills

def graph_nodes(rep_dict):
    graph = nx.MultiDiGraph()
    for rep in rep_dict:
        if 'total' in rep_dict[rep]:
            graph.add_node(rep)
    return graph

def graph_edges(rep_dict, graph):
    for rep in graph.nodes():
        for sponsor in rep_dict[rep]['in_dict']:
            num_sponsorships = rep_dict[rep]['in_dict'][sponsor]
            graph.add_edge(rep, sponsor, weight = num_sponsorships)

#rep_dict = create_rep_weights()
#print(rep_dict)

#graph = graph_nodes(rep_dict)
#graph_edges(rep_dict, graph)
#nx.draw(graph)
#nx.write_gexf(graph, 'sponsors_graph.gexf')








