from helper_functions import open_db, commit_db
from pprint import pprint

house_maj = 218
house_two_third = 290
senate_maj = 255
senate_two_third = 330
president = 500
amendment_pen = -100
vote_bonus = 10
intro = 5

points_dict = {'enacted_veto_override': intro + vote_bonus + senate_maj + vote_bonus + house_maj + vote_bonus + senate_two_third + vote_bonus + house_two_third,
    'enacted_signed': intro + vote_bonus + senate_maj + vote_bonus + house_maj + president,
    'enacted_tendayrule': intro + vote_bonus + senate_maj + vote_bonus + house_maj + president,
    'vetoed_override_fail_second_house': intro + vote_bonus + senate_maj + vote_bonus + house_maj + vote_bonus + senate_two_third + vote_bonus,
    'vetoed_override_fail_originating_senate': intro + vote_bonus + senate_maj + vote_bonus + house_maj + vote_bonus,
    'prov_kill_veto': intro + vote_bonus + senate_maj + vote_bonus + house_maj,
    'vetoed_pocket': intro + vote_bonus + senate_maj + vote_bonus + house_maj,
    'passed_bill': intro + vote_bonus + senate_maj + vote_bonus + house_maj,
    'passed_concurrentres': intro + vote_bonus + senate_maj + vote_bonus + house_maj,
    'pass_back_house': intro + vote_bonus + senate_maj + vote_bonus + house_maj + amendment_pen,
    'fail_second_house': intro + vote_bonus + senate_maj + vote_bonus,
    'pass_back_senate': intro + vote_bonus + senate_maj + vote_bonus + house_maj + amendment_pen,
    'pass_over_senate': intro + vote_bonus + senate_maj,
    'passed_simpleres': intro + vote_bonus + senate_maj,
    'conference_passed_senate': intro + vote_bonus + senate_maj + vote_bonus + house_maj + amendment_pen,
    'prov_kill_pingpongfail': intro + vote_bonus + senate_maj + vote_bonus + house_maj + amendment_pen,
    'conference_passed_house': intro + vote_bonus + senate_maj + vote_bonus + house_maj + amendment_pen,
    'fail_originating_senate': intro + vote_bonus,
    'prov_kill_suspensionfailed': intro + vote_bonus,
    'prov_kill_cloturefailed': intro ,
    'pass_over_house': intro + house_maj,
    'introduced': intro,
    'referred': intro,
    'reported': intro,
    'fail_originating_house': 0}

def find_leadership_scores(c):
    leadership_dict = {}
    r = c.execute('SELECT bill_id, status, sponsor_id, congress FROM bills')
    bills = r.fetchall()
    for bill in bills:
        bill_id = bill[0]
        bill_status = bill[1]
        bill_sponsor_id = bill[2]
        congress = bill[3]

        points = points_dict[bill_status]
        
        if congress not in leadership_dict:
            leadership_dict[congress] = {}
        if bill_sponsor_id not in leadership_dict[congress]:
            leadership_dict[congress][bill_sponsor_id] = 0
        leadership_dict[congress][bill_sponsor_id] += points
    pprint(leadership_dict)
    return leadership_dict

def get_cosponsor_points(c, bill_id):
    r = c.execute('SELECT COUNT(*) FROM cosponsorships WHERE bill = ' + str(bill_id))
    count = r.fetchall()
    count = count[0][0]
    return count

def update_database_with_leadership_scores(c, leadership_dict):
    key = 0
    for congress in leadership_dict:
        for member in leadership_dict[congress]:
            key += 1
            score = leadership_dict[congress][member]
            db_args = [key, member, congress, score, 0, 0]
            c.execute('INSERT INTO leadership VALUES(?,?,?,?,?,?)', db_args)

if __name__ == '__main__':
    c, db = open_db('GovData')
    leadership_dict = find_leadership_scores(c)
    update_database_with_leadership_scores(c, leadership_dict)
    commit_db(db)
