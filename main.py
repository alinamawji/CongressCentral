# application.py
from flask import Flask, render_template, request, send_from_directory
from sqlalchemy.sql import text
from create_db import db, app, Committee, Member, Legislation, Twitter_Account, Financial_Information, Industry_Contributor, Organization_Contributor, Sector_Contributor, Subcommittee, Hearing, Action, Are_Part_Of, Is_Pushed_Through, Discuss

@app.route('/')
def index():
    return render_template('index.html')

ROWS_PER_PAGE = 10
ROWS_PER_PAGE_COMMITTEE = 5

# MEMBERS
@app.route('/members/', methods=['GET', 'POST'])
def members():
    page = request.args.get('page', 1, type=int)
    member = Member.query.paginate(page, per_page=ROWS_PER_PAGE)
    if request.method == 'POST':
        member = Member.query.filter(Member.lname.ilike('%' + str(request.form['user_input']) + '%')).paginate(page=page, per_page=ROWS_PER_PAGE)
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
    legislation = Legislation.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    action = Action.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    member = Member.query.all()
    if request.method == 'POST':
        legislation = Legislation.query.filter(Legislation.bill_number.ilike('%' + str(request.form['user_input']) + '%')).paginate(page=page, per_page=ROWS_PER_PAGE)
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
def api():
    member_list = Member.query.all()
    print(member_list)
    return str([Member.lname for mem in member_list])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
