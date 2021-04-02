# application.py
from flask import Flask, render_template, request, send_from_directory
from sqlalchemy.sql import text
from create_db import db, app, Committee, Member, Legislation, Twitter_Account, Financial_Information, Industry_Contributor, Organization_Contributor, Sector_Contributor, Subcommittee, Hearing, Action, Are_Part_Of, Is_Pushed_Through, Discuss


@app.route('/')
def index():
    return render_template('index.html')

ROWS_PER_PAGE = 10

# MEMBERS
@app.route('/members/', methods=['GET'])
def members():
    page = request.args.get('page', 1, type=int)
    member = Member.query.paginate(page, per_page=ROWS_PER_PAGE)
    return render_template('members.html', member=member)

@app.route('/members/<member_id>')
def individual_member():
    member = Member.query.all()
    committee = Committee.query.all()
    twitter = Twitter_Account.query.all()
    financial = Financial_Information.query.all()
    industry_contributor = Industry_Contributor.query.all()
    organization_contributor = Organization_Contributor.query.all()
    sector_contributor = Sector_Contributor.query.all()
    legislation = db.session.query(legislation).all()
    return render_template('individual_member.html', id=member_id, member=member, committee=committee, twitter=twitter, financial=financial, industry_contributor=industry_contributor, organization_contributor=organization_contributor, sector_contributor=sector_contributor, legislation=legislation)

# COMMITTEES
@app.route('/committees/')
def committees():
    page = request.args.get('page', 1, type=int)
    committee = Committee.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    hearing = Heraring.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    member = Member.query.all()
    return render_template('committees.html', committee=committee, hearing=hearing, is_pushed_through=is_pushed_through, member=member)

# LEGISLATION
@app.route('/legislation/')
def legislation():
    page = request.args.get('page', 1, type=int)
    legislation = Legislation.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    action = Action.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    member = Member.query.all()
    return render_template('legislation.html', legislation=legislation, member=member, action=action, is_pushed_through=is_pushed_through)

@app.route('/legislation/<bill_id>')
def individual_legislation():
    legislation = Legislation.query(legislation).all()
    member = Member.query.all()
    is_pushed_through = Is_Pushed_Through.query.all()
    action = Action.query.all()
    return render_template('individual_legislation.html', id=bill_id,  legislation=legislation, member=member, is_pushed_through=is_pushed_through, action=action)

# ABOUT
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 8080)
