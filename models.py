#!/usr/bin/env python3

# ---------------------------
# ./cs331e-idb/models.py
# Team 19: Alina Mawji, Michael DiLeo, Robert Everson, Andrew Kim
# ---------------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Prerequisite step:
# Please make sure correct path
# assume that username: postgres, password: asd123
# set CREATE DATABASE congress;

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:asd123@localhost:5432/congress')
# For GCP
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgresql://postgres:asd123@35.223.96.67:5432/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

# ------------
# Committee
# ------------
class Committee(db.Model):
    """
    Committee class has 5 attributes
    name (primary key)
    website
    branch
    chair_id
    ranking_id
    """
    __tablename__ = 'committee'

    id = db.Column(db.String(10), nullable = False, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    website = db.Column(db.String(255), nullable = False)
    branch = db.Column(db.String(40), nullable = False)
    chair_id = db.Column(db.String(80))
    ranking_id = db.Column(db.String(80))

    # show the relationship
    subcommittee = db.relationship('Subcommittee', backref = 'committee')
    hearing = db.relationship('Hearing', backref = 'committee')

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'id': self.id,
          'name': self.name,
          'website': self.website,
          'branch': self.branch,
          'chair_id': self.chair_id,
          'ranking_id': self.ranking_id
        }

# ------------
# Member
# ------------
class Member(db.Model):
    """
    Member class has 13 attributes
    id (primary key)
    fname: first name
    lname: last name
    mname: middle name
    namesuffix
    party
    state
    state_rank
    phone
    mailing_address
    url
    votes_w_party
    votes_against_party
    """
    __tablename__ = 'member'

    id = db.Column(db.String(20), nullable = False, primary_key = True)
    fname = db.Column(db.String(20), nullable = False)
    lname = db.Column(db.String(20), nullable = False)
    mname = db.Column(db.String(20))
    namesuffix = db.Column(db.String(20))
    party = db.Column(db.String(10), nullable = False)
    state = db.Column(db.String(10), nullable = False)
    state_rank = db.Column(db.String(10), nullable = False)
    phone = db.Column(db.String(20))
    mailing_address = db.Column(db.String(255))
    url = db.Column(db.String(255), nullable = False)
    votes_w_party = db.Column(db.Integer, nullable = False)
    votes_against_party = db.Column(db.Integer, nullable = False)

    # show the relationship betwenn all entities
    legislation = db.relationship('Legislation', backref = 'member')
    twitter_account = db.relationship('Twitter_Account', backref = 'member')
    financial_info = db.relationship('Financial_Information', backref = 'member')
    industry_contributor = db.relationship('Industry_Contributor', backref = 'member')
    organization_contributor = db.relationship('Organization_Contributor', backref = 'member')
    sector_contributor = db.relationship('Sector_Contributor', backref = 'member')

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'id': self.id,
          'fname': self.fname,
          'lname': self.lname,
          'mname': self.mname,
          'namesuffix': self.namesuffix,
          'party': self.party,
          'state': self.state,
          'state_rank': self.state_rank,
          'phone': self.phone,
          'mailing_address': self.mailing_address,
          'url': self.url,
          'votes_w_party': self.votes_w_party,
          'votes_against_party': self.votes_against_party
        }

# ------------
# Legislation
# ------------
class Legislation(db.Model):
    """
    Legislation class has 5 attributes
    bill_id (primary key)
    cosponsors
    summary
    type
    data_introduced
    member_id (foreign key)
    bill_number
    """
    __tablename__ = 'legislation'

    bill_id = db.Column(db.String(20), nullable = False, primary_key = True)
    cosponsors = db.Column(db.Integer, nullable = False)
    summary = db.Column(db.String(1000), nullable = False)
    type = db.Column(db.String(10))
    date_introduced = db.Column(db.String(20), nullable = False)
    # sponsor_id is same as id in member's attributes.
    sponsor_id = db.Column(db.String(20), db.ForeignKey('member.id'))
    bill_number = db.Column(db.String(20), nullable = False)

    # show the relationship
    action = db.relationship('Action', backref = 'legislation')

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'bill_id': self.bill_id,
          'cosponsors': self.cosponsors,
          'summary': self.summary,
          'type': self.type,
          'date_introduced': self.date_introduced,
          # not sure whether this is right or not about foreign key return
          'sponsor_id': self.sponsor_id,
          'bill_number': self.bill_number
        }

# ------------
# Twitter_Account
# ------------
class Twitter_Account(db.Model):
    """
    Twitter_Account class has 6 attributes
    twitter_handle (primary key)
    member_id (foreign key)
    number_following
    number_followers
    number_tweets
    timeline_html
    """
    __tablename__ = 'twitter_account'

    twitter_handle = db.Column(db.String(40), primary_key = True)
    member_id = db.Column(db.String(20), db.ForeignKey('member.id'))
    number_following = db.Column(db.Integer)
    number_followers = db.Column(db.Integer)
    number_tweets = db.Column(db.Integer)
    timeline_html = db.Column(db.String(255))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'twitter_handle': self.twitter_handle,
          'member_id': self.member_id,
          'number_following': self.number_following,
          'number_followers': self.number_followers,
          'number_tweets': self.number_tweets,
          'timeline_html': self.timeline_html
        }

# ------------
# Financial_Information
# ------------
class Financial_Information(db.Model):
    """
    Financial_Information class has 2 attributes
    crp_id (primary key)
    member_id (foreign key)
    """
    __tablename__ = 'financial_information'

    crp_id = db.Column(db.String(20), primary_key = True)
    member_id = db.Column(db.String(20), db.ForeignKey('member.id'))

    # show the relationship
    industry_contr = db.relationship('Industry_Contributor', backref = 'financial_information')
    organ_contr = db.relationship('Organization_Contributor', backref = 'financial_information')
    sect_contr = db.relationship('Sector_Contributor', backref = 'financial_information')

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'crp_id': self.crp_id,
          'member_id': self.member_id
        }

# ------------
# Industry_Contributor
# ------------
class Industry_Contributor(db.Model):
    """
    Industry_Contributor class has 4 attributes
    industry_name (primary key)
    crp_id (foreign key)
    member_id
    total
    """
    __tablename__ = 'industry_contributor'

    industry_name = db.Column(db.String(100), primary_key = True)
    crp_id = db.Column(db.String(20), db.ForeignKey('financial_information.crp_id'), primary_key = True)
    member_id = db.Column(db.String(20), db.ForeignKey('member.id'))
    total = db.Column(db.String(20))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'industry_name': self.industry_name,
          'crp_id': self.crp_id,
          'member_id': self.member_id,
          'total': self.total
        }

# ------------
# Organization_Contributor
# ------------
class Organization_Contributor(db.Model):
    """
    Organization_Contributor class has 4 attributes
    org_name (primary key)
    crp_id (foreign key)
    member_id (foreign key)
    total
    """
    __tablename__ = 'organ_contributor'

    org_name = db.Column(db.String(100), primary_key = True)
    crp_id = db.Column(db.String(20), db.ForeignKey('financial_information.crp_id'), primary_key = True)
    member_id = db.Column(db.String(20), db.ForeignKey('member.id'))
    total = db.Column(db.String(20))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'org_name': self.org_name,
          'crp_id': self.crp_id,
          'member_id': self.member_id,
          'total': self.total
        }

# ------------
# Sector_Contributor
# ------------
class Sector_Contributor(db.Model):
    """
    Sector_Contributor class has 4 attributes
    sector_name (primary key)
    crp_id (foreign key)
    member_id (foreign key)
    total
    """
    __tablename__ = 'sector_contributor'

    sector_name = db.Column(db.String(100), primary_key = True)
    crp_id = db.Column(db.String(20), db.ForeignKey('financial_information.crp_id'), primary_key = True)
    member_id = db.Column(db.String(20), db.ForeignKey('member.id'))
    total = db.Column(db.String(20))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'sector_name': self.org_name,
          'crp_id': self.crp_id,
          'member_id': self.member_id,
          'total': self.total
        }

# ------------
# Subcommittee
# ------------
class Subcommittee(db.Model):
    """
    Subcommittee class has 2 attributes
    name (primary key)
    committee_name (foreign key)
    """
    __tablename__ = 'subcommittee'

    name = db.Column(db.String(150), primary_key = True)
    committee_id = db.Column(db.String(10), db.ForeignKey('committee.id'))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'sector_name': self.name,
          'committee_id': self.committee_id
        }

# ------------
# Hearing
# ------------
class Hearing(db.Model):
    """
    Hearing class has 5 attributes
    date (primary key)
    committee_name (foreign key)
    time (primary key)
    location (primary key)
    description
    """
    __tablename__ = 'hearing'

    date = db.Column(db.String(20), primary_key = True)
    committee_id = db.Column(db.String(10), db.ForeignKey('committee.id'), primary_key = True)
    time = db.Column(db.String(20), primary_key = True)
    location = db.Column(db.String(20), primary_key = True)
    description = db.Column(db.String(4000))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'date': self.date,
          'committee_id': self.committee_id,
          'time': self.time,
          'location': self.location,
          'description': self.description
        }

# ------------
# Action
# ------------
class Action(db.Model):
    """
    Action class has 4 attributes
    action_id (primary key)
    bill_id (foreign key)
    date
    description
    """
    __tablename__ = 'action'

    action_id = db.Column(db.String(20), primary_key = True)
    bill_id = db.Column(db.String(80), db.ForeignKey('legislation.bill_id'), primary_key = True)
    date = db.Column(db.String(20))
    description = db.Column(db.String(1500))

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'action_id': self.action_id,
          'bill_id': self.bill_id,
          'date': self.date,
          'description': self.description
        }

# ------------
# Are_Part_Of
# ------------
class Are_Part_Of(db.Model):
    """
    Are_Part_Of class has 2 attributes
    committee_name (foreign key)
    member_id (foreign key)
    """
    __tablename__ = 'are_part_of'

    committee_id = db.Column(db.String(10), primary_key = True)
    member_id = db.Column(db.String(20), primary_key = True)


    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'committee_id': self.committee_id,
          'member_id': self.member_id
        }

# ------------
# Is_Pushed_Through
# ------------
class Is_Pushed_Through(db.Model):
    """
    Is_Pushed_Through class has 2 attributes
    committee_name (foreign key)
    bill_id (foreign key)
    """
    __tablename__ = 'is_pushed_through'

    committee_id = db.Column(db.String(10), primary_key = True)
    bill_id = db.Column(db.String(80), primary_key = True)

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'committee_id': self.committee_id,
          'bill_id': self.bill_id
        }

# ------------
# Discuss
# ------------
class Discuss(db.Model):
    """
    Discuss class has 4 attributes
    hearing_date (foreign key)
    hearing_time (foreign key)
    hearing_location (foreign key)
    bill_ID (foreign key)
    """
    __tablename__ = 'discuss'

    hearing_date = db.Column(db.String(20), primary_key = True)
    hearing_time = db.Column(db.String(20), primary_key = True)
    hearing_location = db.Column(db.String(20), primary_key = True)
    bill_id = db.Column(db.String(80), primary_key = True)

    # ------------
    # serialize
    # ------------
    def serialize(self):
       """
       returns a dictionary
       """
       return {
          'hearing_date': self.hearing_date,
          'hearing_time': self.hearing_time,
          'hearing_location': self.hearing_location,
          'bill_id': self.bill_id
        }

db.drop_all()
db.create_all()
