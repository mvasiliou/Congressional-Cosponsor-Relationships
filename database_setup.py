#Database Set Up Code
import sqlite3
from helper_functions import make_url_request, open_db, commit_db

def create_tables(c):
    c.execute('CREATE TABLE senators(id integer PRIMARY KEY, first text, last text, party text, class text, rank text, state text)')
    c.execute('CREATE TABLE bills(bill_id integer PRIMARY KEY, title text, status text, introduced_date text, sponsor_id integer)')
    c.execute('CREATE TABLE cosponsorships(action_id integer PRIMARY KEY, bill integer, cosponsor integer, joined_date text)')

def add_rep_to_db(c):
    url = "https://www.govtrack.us/api/v2/role?current__exact=true&&role_type__exact=senator"
    data = make_url_request(url)
    for senator in data['objects']:
        s_id = senator['person']['id']
        first = senator['person']['firstname']
        last = senator['person']['lastname']
        party = senator['party']
        s_class = senator['senator_class']
        rank = senator['senator_rank_label']
        state = senator['state']
        db_args = (s_id, first, last, party, s_class, rank, state)
        c.execute('INSERT INTO senators VALUES(?,?,?,?,?,?,?)', db_args)  

def add_sponsored_bills(c):
    r = c.execute('SELECT id FROM senators')
    senators = r.fetchall()
    for s_id in senators:
        s_id = s_id[0]
        url = "https://www.govtrack.us/api/v2/bill?limit=6000&&introduced_date__gt=2015-01-01&&sponsor__exact=" + str(s_id)
        data = make_url_request(url)
        for bill in data['objects']:
            bill_id = bill['id']
            print('Bill Num:', bill_id)
            title = bill['title']
            status = bill['current_status']
            introduced_date = bill['introduced_date']
            sponsor_id = bill['sponsor']['id']
            db_args = (bill_id, title, status, introduced_date, sponsor_id)
            c.execute('INSERT INTO bills VALUES(?,?,?,?,?)', db_args)

def add_cosponsorships(c):
    r = c.execute('SELECT bill_id FROM bills')
    bills = r.fetchall()
    for bill in bills:
        bill = bill[0]
        url = 'https://www.govtrack.us/api/v2/cosponsorship?bill__exact=' + str(bill)
        data = make_url_request(url)
        for person in data['objects']:
            action_id = person['id']
            print("Cospon Num:", action_id)
            cosponsor = person['person']
            joined_date = person['joined']
            db_args = (action_id, bill, cosponsor, joined_date)
            c.execute('INSERT INTO cosponsorships VALUES(?,?,?,?)', db_args)

if __name__ == '__main__':
    c, db = open_db('GovData')
    create_tables(c)
    add_rep_to_db(c)
    add_sponsored_bills(c)
    add_cosponsorships(c)
    commit_db(db)
