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

# API for listing all member names and IDs
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
    for committee in committee_list:
        for subcommittee in subcommittee_list:
            if subcommittee.committee_id == committee.id:
                response.append({str(committee.name) : str(subcommittee.name)})
    
    return make_response({'Committees and Subcommittees' : response}, 200)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
