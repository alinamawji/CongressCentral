import json
from models import app, db, Committee, Member, Legislation, Twitter_Account, Financial_Information, Industry_Contributor, Organization_Contributor, Sector_Contributor, Subcommittee, Hearing, Action, Are_Part_Of, Is_Pushed_Through, Discuss

# ------------
# load_json: load json file from each table
# ------------
def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    file = open(filename)
    jsn = json.load(file)
    file.close()

    return jsn

# ------------
# create_Committees
# ------------
def create_Committees():
    committee = load_json('./api_calls/committees_table.json')

    for one_committee in committee:
        id = one_committee['id']
        name = one_committee['name']
        website = one_committee['website']
        branch = one_committee['branch']
        chair_id = one_committee['chair_id']
        ranking_id = one_committee['ranking_id']
        newCommittee = Committee(id = id, name = name, website = website, branch = branch, chair_id = chair_id, ranking_id = ranking_id)

        # add it to our session
        db.session.add(newCommittee)
        # commit the session to our DB. 
        db.session.commit()

# ------------
# create_Members
# ------------
def create_Members():
    member = load_json('./api_calls/members_table.json')

    for one_member in member:
        id = one_member['id']
        fname = one_member['fname']
        lname = one_member['lname']
        mname = one_member['mname']
        namesuffix = one_member['namesuffix']
        party = one_member['party']
        state = one_member['state']
        state_rank = one_member['state_rank']
        phone = one_member['phone']
        mailing_address = one_member['mailing_address']
        url = one_member['url']
        votes_w_party = one_member['votes_w_party']
        votes_against_party = one_member['votes_against_party']
        newMember = Member(id = id, fname = fname, lname = lname, mname = mname, namesuffix = namesuffix, party = party, state = state, state_rank = state_rank, phone = phone, mailing_address = mailing_address, url = url, votes_w_party = votes_w_party, votes_against_party = votes_against_party)

        # add it to our session
        db.session.add(newMember)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Legislation
# ------------

def create_Legislation():
    legislation = load_json('./api_calls/legislation_table.json')
    
    for legi_info in legislation:
        bill_id = legi_info['bill_id']
        cosponsors = legi_info['cosponsors']
        summary = legi_info['summary']
        type = legi_info['type']
        date_introduced = legi_info['date_introduced']
        sponsor_id = legi_info['sponsor_id']
        bill_number = legi_info['bill_number']
        newLegislation = Legislation(bill_id = bill_id, cosponsors = cosponsors, summary = summary, type = type, date_introduced = date_introduced, sponsor_id = sponsor_id, bill_number = bill_number)

        # add it to our session
        db.session.add(newLegislation)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Twitter_accounts
# ------------


def create_Twitter_accounts():
    Twitter_accounts = load_json('./api_calls/twitter_account_table.json')
    
    for account in Twitter_accounts:
        member_id = account['member_id']
        twitter_handle = account['twitter_handle']
        number_following = account['number_following']
        number_followers = account['number_followers']
        number_tweets = account['number_tweets']
        timeline_html = account['timeline_html']
        newAccount = Twitter_Account(member_id = member_id, twitter_handle = twitter_handle, number_following = number_following, number_followers = number_followers, number_tweets = number_tweets, timeline_html = timeline_html)

        # add it to our session
        db.session.add(newAccount)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Financial_Information
# ------------


def create_Financial_Information():
    F_Info = load_json('./api_calls/financial_information_table.json')
    for f_info in F_Info:
        member_id = f_info['member_id']
        crp_id = f_info['crp_id']
        newF_Info = Financial_Information(member_id = member_id, crp_id = crp_id)

        # add it to our session
        db.session.add(newF_Info)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Industry_contributors
# ------------


def create_Industry_contributors():
    IC_Info = load_json('./api_calls/industry_contributors_table.json')
    for info in IC_Info:
        crp_id = info['crp_id']
        industry_name = info['industry_name']
        total = info['total']

        newIC_Info = Industry_Contributor(crp_id = crp_id, industry_name = industry_name, total = total)

        # add it to our session
        db.session.add(newIC_Info)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Organization_contributors
# ------------


def create_Organization_contributors():
    OC_Info = load_json('./api_calls/organization_contributors_table.json')
    for info in OC_Info:
        crp_id = info['crp_id']
        org_name = info['org_name']
        total = info['total']

        newOC_Info = Organization_Contributor(crp_id = crp_id, org_name = org_name, total = total)

        # add it to our session
        db.session.add(newOC_Info)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Sector_contributors
# ------------


def create_Sector_contributors():
    SC_Info = load_json('./api_calls/sector_contributors_table.json')
    for info in SC_Info:
        crp_id = info['crp_id']
        sector_name = info['sector_name']
        total = info['total']

        newSC_Info = Sector_Contributor(crp_id = crp_id, sector_name = sector_name, total = total)

        # add it to our session
        db.session.add(newSC_Info)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Subcommittees
# ------------


def create_Subcommittees():
    subcommittees = load_json('./api_calls/subcommittees_table.json')
    for subcommittee_info in subcommittees:
        name = subcommittee_info['name']
        committee_id = subcommittee_info['committee_id']

        newSubcommittee = Subcommittee(name = name, committee_id = committee_id)

        # add it to our session
        db.session.add(newSubcommittee)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Hearings
# ------------


def create_Hearings():
    Hearings = load_json('./api_calls/hearings_table.json')
    for info in Hearings:
        date = info['date']
        committee_id = info['committee_id']
        time = info['time']
        location = info['location']
        description = info['description']

        newHearing = Hearing(date = date, committee_id = committee_id, time = time, location = location, description = description)
        # add it to our session
        db.session.add(newHearing)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Actions
# ------------


def create_Actions():
    Actions = load_json('./api_calls/actions_table.json')
    for info in Actions:
        action_id = info['action_id']
        bill_id = info['bill_id']
        date = info['date']
        description = info['description']

        newAction = Action(action_id = action_id, bill_id = bill_id, date = date, description = description)
        # add it to our session
        db.session.add(newAction)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Be_Part_of
# ------------


def create_Be_Part_of():
    Parts = load_json('./api_calls/are_part_of_table.json')
    for part in Parts:
        committee_id = part['committee_id']
        member_id = part['member_id']

        newPart = Are_Part_Of(committee_id = committee_id, member_id = member_id)
        # add it to our session
        db.session.add(newPart)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Be_Pushed_through
# ------------


def create_Be_Pushed_through():
    Pushs = load_json('./api_calls/is_pushed_through_table.json')
    for push in Pushs:
        committee_id = push['committee_id']
        bill_id = push['bill_id']

        newPush = Is_Pushed_Through(committee_id = committee_id, bill_id = bill_id)
        # add it to our session
        db.session.add(newPush)
        # commit the session to our DB.
        db.session.commit()

# ------------
# create_Discuss
# ------------


def create_Discuss():
    discuss = load_json('./api_calls/discuss_table.json')
    for content in discuss:
        hearing_date = content['hearing_date']
        hearing_time = content['hearing_time']
        hearing_location = content['hearing_location']
        bill_id = content['bill_id']

        newDiscuss = Discuss(hearing_date = hearing_date, hearing_time = hearing_time, hearing_location = hearing_location, bill_id = bill_id)
        # add it to our session
        db.session.add(newDiscuss)
        # commit the session to our DB.
        db.session.commit()

create_Committees()
create_Members()
create_Legislation()
create_Twitter_accounts()
create_Financial_Information()
create_Industry_contributors()
create_Organization_contributors()
create_Sector_contributors()
create_Subcommittees()
create_Hearings()
create_Actions()
create_Be_Part_of()
create_Be_Pushed_through()
create_Discuss()
