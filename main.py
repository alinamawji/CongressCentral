# application.py
from flask import Flask, render_template, request, send_from_directory, url_for, redirect, json, jsonify, Response, make_response
from sqlalchemy.sql import text
from create_db import db, app, Committee, Member, Legislation, Twitter_Account, Financial_Information, Industry_Contributor, Organization_Contributor, Sector_Contributor, Subcommittee, Hearing, Action, Are_Part_Of, Is_Pushed_Through, Discuss

ROWS_PER_PAGE_MEMBERS = 20
ROWS_PER_PAGE_COMMITTEE = 10
ROWS_PER_PAGE_LEG = 15

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        member = Member.query.filter(Member.lname.ilike('%' + str(request.form['user_input']) + '%') |
            Member.fname.ilike('%' + str(request.form['user_input']) + '%') |
            Member.state.ilike('%' + str(request.form['user_input']) + '%') |
            Member.state_rank.ilike('%' + str(request.form['user_input']) + '%') |
            Member.party.ilike('%' + str(request.form['user_input']) + '%'))
        committee = Committee.query.filter(Committee.name.ilike('%' + str(user_input) + '%'))
        hearing = Hearing.query.all()
        subcommittees = Subcommittee.query.all()
        are_part_of = Are_Part_Of.query.all()
        legislation = Legislation.query.filter(Legislation.bill_number.ilike('%' + str(user_input) + '%'))
        action = Action.query.all()
        is_pushed_through = Is_Pushed_Through.query.all()
        return render_template('index_search_results.html', user_input=user_input, member=member, legislation=legislation, action=action, is_pushed_through=is_pushed_through, committee=committee, hearing=hearing, subcommittees=subcommittees, are_part_of=are_part_of)
    else:
        return render_template('index.html')

# MEMBER
@app.route('/members/', methods=['GET', 'POST'])
def members():
    page = request.args.get('page', 1, type=int)
    member = Member.query.paginate(page, per_page=ROWS_PER_PAGE_MEMBERS)
    if request.method == 'POST':
        member = Member.query.filter(Member.lname.ilike('%' + str(request.form['user_input']) + '%') |
            Member.fname.ilike('%' + str(request.form['user_input']) + '%') |
            Member.state.ilike('%' + str(request.form['user_input']) + '%') |
            Member.state_rank.ilike('%' + str(request.form['user_input']) + '%') |
            Member.party.ilike('%' + str(request.form['user_input']) + '%')).paginate(page=page, per_page=ROWS_PER_PAGE_MEMBERS)
    else:
        pass

    return render_template('members.html', member=member)

@app.route('/members/<member_id>')
def individual_member(member_id):
    member = Member.query.all()
    committee = Committee.query.all()
    twitter = Twitter_Account.query.all()
    financial = Financial_Information.query.all()
    industry_contributor = Industry_Contributor.query.all()
    organization_contributor = Organization_Contributor.query.all()
    sector_contributor = Sector_Contributor.query.all()
    legislation = Legislation.query.all()
    are_part_of = Are_Part_Of.query.all()
    return render_template('individual_member.html', member_id=member_id, member=member, committee=committee, twitter=twitter, financial=financial, industry_contributor=industry_contributor, organization_contributor=organization_contributor, sector_contributor=sector_contributor, legislation=legislation, are_part_of=are_part_of)

# COMMITTEES
@app.route('/committees/', methods=['GET','POST'])
def committees():
    page = request.args.get('page', 1, type=int)
    committee = Committee.query.paginate(page=page, per_page=ROWS_PER_PAGE_COMMITTEE)
    hearing = Hearing.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    member = Member.query.all()
    subcommittees = Subcommittee.query.all()
    are_part_of = Are_Part_Of.query.all()
    if request.method == 'POST':
        committee = Committee.query.filter(Committee.name.ilike('%' + str(request.form['user_input']) + '%')).paginate(page=page, per_page=ROWS_PER_PAGE_COMMITTEE)
    else:
        pass

    return render_template('committees.html', committee=committee, hearing=hearing, is_pushed_through=is_pushed_through, member=member, subcommittees=subcommittees, are_part_of=are_part_of)

@app.route('/committee/<committee_id>')
def individual_committee(committee_id):
    member = Member.query.all()
    committee = Committee.query.all()
    hearing = Hearing.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    are_part_of = Are_Part_Of.query.all()
    discuss = Discuss.query.all()
    subcommittees = Subcommittee.query.all()
    legislation = Legislation.query.all()
    return render_template('individual_committee.html', id=committee_id, member=member, committee=committee, hearing=hearing, is_pushed_through=is_pushed_through, are_part_of=are_part_of, discuss=discuss, subcommittees=subcommittees, legislation=legislation)

# LEGISLATION
@app.route('/legislation/', methods=['GET','POST'])
def legislation():
    page = request.args.get('page', 1, type=int)
    legislation = Legislation.query.paginate(page=page, per_page=ROWS_PER_PAGE_LEG)
    action = Action.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    member = Member.query.all()
    if request.method == 'POST':
        legislation = Legislation.query.filter(Legislation.bill_number.ilike('%' + str(request.form['user_input']) + '%') | Legislation.summary.ilike('%' + str(request.form['user_input']) + '%')).paginate(page=page, per_page=ROWS_PER_PAGE_LEG)
    else:
        pass

    return render_template('legislation.html', legislation=legislation, member=member, action=action, is_pushed_through=is_pushed_through)

@app.route('/legislation/<bill_id>')
def individual_legislation(bill_id):
    legislation = Legislation.query.all()
    member = Member.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    action = Action.query.all()
    committee = Committee.query.all()
    return render_template('individual_legislation.html', bill_id=bill_id,  legislation=legislation, member=member, is_pushed_through=is_pushed_through, action=action, committee=committee)

# ABOUT
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/api/')
def apiTest():
    member_list = Member.query.all()
    print(member_list)
    return str([Member.lname for mem in member_list])

# API for listing all member names and ID
@app.route('/members/json/')
def membersjson():
    response = list()

    member_list = Member.query.all()
    for mem in member_list:
        response.append({'ID' : str(mem), 'Name' : str(mem.fname) + ' ' + str(mem.lname)})

    return make_response({'Members' : response}, 200)

# API for listing all committees and subcommittees
@app.route('/committees/json/')
def committeesjson():
    response = list()

    committee_list = Committee.query.all()
    subcommittee_list = Subcommittee.query.all()
    for j in range(len(committee_list)):
        has_sub = False
        for i in range(len(subcommittee_list)):
            if subcommittee_list[i].committee_id == committee_list[j].id:
                response.append({str(committee_list[j].name) : str(subcommittee_list[i].name)})
                has_sub = True
            elif has_sub:
                if j < len(committee_list) - 1:
                    j += 1
                else:
                    break
            else:
                response.append({str(committee_list[j].name) : 'No subcommittees'})
                if j < len(committee_list) - 1:
                    j += 1
                else:
                    break
    
    return make_response({'Committees and Subcommittees' : response}, 200)

# API for listing all legislation
@app.route('/legislation/json/')
def legislationjson():
    response = list()

    legislation_list = Legislation.query.all()
    pushed_list = Is_Pushed_Through.query.all()
    committee_list = Committee.query.all()
    for legislation in legislation_list:
        response.append({'Bill ID' : str(legislation.bill_id), 'Bill Summary' : str(legislation.summary), 'Date introduced' : str(legislation.date_introduced)})
    
    return make_response({'Legislation Bill IDs, Summary and Date Introduced' : response}, 200)

# Endpoint API for listing all information about a specific user ID
@app.route('/members/<member_id>/json/')
def member_id_json(member_id):
    response = list()

    member_list = Member.query.all()
    legislation_list = Legislation.query.all()
    account_list = Twitter_Account.query.all()
    finan_info = Financial_Information.query.all()
    Indus_info = Industry_Contributor.query.all()
    Organ_info = Organization_Contributor.query.all()
    sector_info = Sector_Contributor.query.all()
    part_info = Are_Part_Of.query.all()

    for i in range(len(member_list)):
        if member_list[i].id == member_id:
            response.append({'Member ID' : str(member_list[i].id), 'First name' : str(member_list[i].fname), 'Middle name' : str(member_list[i].mname), 'Last name' : str(member_list[i].lname), 'Name suffix' : str(member_list[i].namesuffix), 'Party' : str(member_list[i].party), 'State' : str(member_list[i].state), 'State rank' : str(member_list[i].state_rank), 'Phone' : str(member_list[i].phone), 'Mailing address' : str(member_list[i].mailing_address), 'Url' : str(member_list[i].url), 'Votes with party' : str(member_list[i].votes_w_party), 'Votes against party' : str(member_list[i].votes_against_party)})
       
    for i in range(len(legislation_list)):
        if legislation_list[i].sponsor_id == member_id:
            response.append({'Bill ID' : str(legislation_list[i].bill_id), 'Co-sponsors' : legislation_list[i].cosponsors, 'Summary' : str(legislation_list[i].summary), 'Type' : str(legislation_list[i].type), 'Introduced date' : str(legislation_list[i].date_introduced), 'Sponsor ID' : str(legislation_list[i].sponsor_id), 'Bill number' : str(legislation_list[i].bill_number)})

    for i in range(len(account_list)):
        if account_list[i].member_id == member_id:
            response.append({'Twitter handle' : str(account_list[i].twitter_handle), 'Twitter following' : str(account_list[i].number_following), 'Twitter followers' : str(account_list[i].number_followers), 'Number tweets' : str(account_list[i].number_tweets), 'Timeline html' : str(account_list[i].timeline_html)})

    for i in range(len(finan_info)):
        if finan_info[i].member_id == member_id:
            response.append({'Crp ID' : str(finan_info[i].crp_id)})

    for i in range(len(Indus_info)):
        if Indus_info[i].member_id == member_id:
            response.append({'Industry name' : str(Indus_info[i].industry_name), 'Industry Contributor total' : str(Indus_info[i].total)})

    for i in range(len(Organ_info)):
        if Organ_info[i].member_id == member_id:
            response.append({'Organization Name' : str(Organ_info[i].org_name), 'Organization Contributor total' : str(Organ_info[i].total)})

    for i in range(len(sector_info)):
        if sector_info[i].member_id == member_id:
            response.append({'Sector Name' : str(Organ_info[i].org_name), 'Sector Contributor total' : str(Organ_info[i].total)})

    for i in range(len(part_info)):
        if part_info[i].member_id == member_id:
            response.append({'Committee ID' : str(part_info[i].committee_id)})

    return make_response({'A specific member information' : response}, 200)
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
