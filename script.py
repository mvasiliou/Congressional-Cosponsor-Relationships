import json
from pprint import pprint
import urllib.request


def create_rep_weights():
    rep_dict = {}
    get_rep_codes(rep_dict)
    
    num = 0
    for rep in rep_dict:
        num += 1
        print(num)
        get_rep_weight(rep, rep_dict)
    pprint(rep_dict)    
    
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


create_rep_weights()