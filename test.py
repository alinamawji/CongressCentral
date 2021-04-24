#!/usr/bin/env python3

# -------
# imports
# -------

import os
import sys
import unittest
from models import db, Committee, Member, Legislation, Twitter_Account, Financial_Information, Industry_Contributor, Organization_Contributor, Sector_Contributor, Subcommittee, Hearing, Action, Are_Part_Of, Is_Pushed_Through, Discuss

# -----------
# DBTestCases
# -----------
class DBTestCases(unittest.TestCase):
    # ---------
    # insertion
    # ---------

    def test_source_insert_1(self):
        s = Committee(id="ABCD",name="committee1", website="https://www.committee1.com/", branch="senate", chair_id=1234, ranking_id=5678)
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Committee).filter_by(id = "ABCD").one()
        self.assertEqual(str(r.id), "ABCD")

        # need to test and after that input delete later
        #db.session.query(Committee).filter_by(id = "ABCD").delete()
        #db.session.commit()

    def test_source_insert_2(self):
        s = Member(id="987", fname="Mr", lname="Bean", mname="L", namesuffix="Jr.", party="party1", state="state1", state_rank="rank1", phone=5121234567, mailing_address="123 St", votes_w_party=95, votes_against_party=5, url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Member).filter_by(id = "987").one()
        self.assertEqual(str(r.id), "987")
        
        # To show the relationship of primary and foreign key for next test case, comment delete command
        #db.session.query(Member).filter_by(id = "987").delete()
        #db.session.commit()

    def test_source_insert_3(self):
        # make sure a foreign key variable such as sponsor_id(member_id) should exist in a linked database, which has its primary key
        s = Legislation(bill_id="123", cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", sponsor_id="987", bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Legislation).filter_by(bill_id = "123").one()
        self.assertEqual(str(r.bill_id), "123")

        db.session.query(Legislation).filter_by(bill_id = "123").delete()
        db.session.commit()

    def test_source_insert_4(self):
        s = Twitter_Account(twitter_handle="SenateDoe", number_following=0, number_followers=0, number_tweets=0, timeline_html="")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Twitter_Account).filter_by(twitter_handle = "SenateDoe").one()
        self.assertEqual(str(r.twitter_handle), "SenateDoe")

        db.session.query(Twitter_Account).filter_by(twitter_handle = "SenateDoe").delete()
        db.session.commit()

    def test_source_insert_5(self):
        s = Financial_Information(crp_id="N000000")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Financial_Information).filter_by(crp_id = "N000000").one()
        self.assertEqual(str(r.crp_id), "N000000")


    def test_source_insert_6(self):
        s = Industry_Contributor(industry_name="Public Health", total="", crp_id="N000000")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Industry_Contributor).filter_by(industry_name = "Public Health").one()
        self.assertEqual(str(r.total), "")
        db.session.query(Industry_Contributor).filter_by(industry_name = "Public Health").delete()
        db.session.commit()

    def test_source_insert_7(self):
        s = Organization_Contributor(org_name="UT Austin", total="", crp_id="N000000")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Organization_Contributor).filter_by(org_name = "UT Austin").one()
        self.assertEqual(str(r.total), "")

        db.session.query(Organization_Contributor).filter_by(org_name = "UT Austin").delete()
        db.session.commit()



    def test_source_insert_8(self):
        s = Sector_Contributor(sector_name="IT", total="", crp_id="N000000")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Sector_Contributor).filter_by(sector_name = "IT").one()
        self.assertEqual(str(r.total), "")

        db.session.query(Sector_Contributor).filter_by(crp_id = "N000000").delete()
        db.session.commit()

        db.session.query(Sector_Contributor).filter_by(sector_name = "IT").delete()
        db.session.commit()


    def test_source_insert_9(self):
        s = Subcommittee(name="Diplomacy Department")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Subcommittee).filter_by(name = "Diplomacy Department").one()
        self.assertEqual(str(r.name), "Diplomacy Department")

        db.session.query(Subcommittee).filter_by(name = "Diplomacy Department").delete()
        db.session.commit()


    def test_source_insert_10(self):
        s = Hearing(date="2000/1/1", committee_id="ABCD", time="00:00:00", location="KT-000", description="~")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Hearing).filter_by(date = "2000/1/1").one()
        self.assertEqual(str(r.time), "00:00:00")

        db.session.query(Hearing).filter_by(date = "2000/1/1").delete()
        db.session.commit()


    def test_source_insert_11(self):
        db.session.query(Member).filter_by(id = "987").delete()
        db.session.commit()
        
        s = Member(id="987", fname="Mr", lname="Bean", mname="L", namesuffix="Jr.", party="party1", state="state1", state_rank="rank1", phone=5121234567, mailing_address="123 St", votes_w_party=95, votes_against_party=5, url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        s = Legislation(bill_id="123", cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", sponsor_id="987", bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        s = Action(action_id="0", bill_id="123", date="2000/12/31", description="bill id 123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Action).filter_by(action_id = "0").one()
        self.assertEqual(str(r.description), "bill id 123")

        db.session.query(Action).filter_by(action_id = "0").delete()
        db.session.commit()


    def test_source_insert_12(self):
        s = Are_Part_Of(committee_id="ABCD", member_id="987")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Are_Part_Of).filter_by(committee_id = "ABCD").one()
        self.assertEqual(str(r.committee_id), "ABCD")

        db.session.query(Are_Part_Of).filter_by(committee_id = "ABCD").delete()
        db.session.commit()

    def test_source_insert_13(self):
        s = Is_Pushed_Through(committee_id="ABCD", bill_id="123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Is_Pushed_Through).filter_by(committee_id = "ABCD").one()
        self.assertEqual(str(r.bill_id), "123")

        db.session.query(Is_Pushed_Through).filter_by(committee_id = "ABCD").delete()
        db.session.commit()

    def test_source_insert_14(self):
        s = Discuss(hearing_date="0000-00-00", bill_id="123", hearing_time="23:59:59", hearing_location="SK-000")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Discuss).filter_by(hearing_date = "0000-00-00").one()
        self.assertEqual(str(r.hearing_date), "0000-00-00")

        db.session.query(Discuss).filter_by(hearing_date = "0000-00-00").delete()
        db.session.commit()

        db.session.query(Legislation).filter_by(bill_id = "123").delete()
        db.session.commit()

        db.session.query(Committee).filter_by(id = "ABCD").delete()
        db.session.commit()

        db.session.query(Member).filter_by(id = "987").delete()
        db.session.commit()

    def test_source_update_1(self):
        s = Committee(id = "EFGH", name="committee1", website="https://www.committee1.com/", branch="senate", chair_id="1234", ranking_id="5678")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Committee).filter_by(id = "EFGH").one()
        r.branch = "house"
        self.assertEqual(str(r.branch), "house")


    def test_source_update_2(self):
        
        s = Member(id="678", fname="Mr", lname="Bean", mname="L", namesuffix="Jr.", party="party1", state="state1", state_rank="rank1", phone="5121234567", mailing_address="123 St", votes_w_party=95, votes_against_party=5, url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Member).filter_by(id = "678").one()
        r.party = "party2"
        self.assertEqual(str(r.party), "party2")

        # comment this for next testcase
        #db.session.query(Member).filter_by(id = "678").delete()
        #db.session.commit()


    def test_source_update_3(self):
        # make sure a foreign key variable should exist in a linked database, which has its primary key
        s = Legislation(bill_id="456", cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", sponsor_id="678", bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Legislation).filter_by(bill_id = "456").one()
        r.cosponsors = 5
        self.assertEqual(str(r.cosponsors), "5")

        #db.session.query(Legislation).filter_by(bill_id = "456").delete()
        #db.session.commit()

    def test_source_update_4(self):
        s = Twitter_Account(twitter_handle="SenateJohn", number_following=0, number_followers=0, number_tweets=0, timeline_html="")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Twitter_Account).filter_by(twitter_handle = "SenateJohn").one()
        r.number_following = 300000
        self.assertEqual(r.number_following, 300000)

        db.session.query(Twitter_Account).filter_by(twitter_handle = "SenateJohn").delete()
        db.session.commit()

    def test_source_update_5(self):
        s = Financial_Information(crp_id="N999999")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Financial_Information).filter_by(crp_id = "N999999").one()
        r.crp_id = "N777777"
        self.assertEqual(str(r.crp_id), "N777777")


    def test_source_update_6(self):
        s = Industry_Contributor(industry_name="Gas Oil", total="1000000", crp_id="N777777")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Industry_Contributor).filter_by(industry_name = "Gas Oil").one()
        r.industry_name = "Natural Gas"
        self.assertEqual(str(r.industry_name), "Natural Gas")

        db.session.query(Industry_Contributor).filter_by(industry_name = "Natural Gas").delete()
        db.session.commit()

    def test_source_update_7(self):
        s = Organization_Contributor(org_name="U of Arizona", total="", crp_id="N777777")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Organization_Contributor).filter_by(org_name = "U of Arizona").one()
        r.org_name = "U of Michigan"
        self.assertEqual(str(r.org_name), "U of Michigan")

        db.session.query(Organization_Contributor).filter_by(org_name = "U of Michigan").delete()
        db.session.commit()

    def test_source_update_8(self):
        s = Sector_Contributor(sector_name="Uncategorized", total="40000", crp_id="N777777")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Sector_Contributor).filter_by(sector_name = "Uncategorized").one()
        r.sector_name = "ETC"
        self.assertEqual(str(r.sector_name), "ETC")

        db.session.query(Sector_Contributor).filter_by(crp_id = "N777777").delete()
        db.session.commit()

        db.session.query(Sector_Contributor).filter_by(sector_name = "ETC").delete()
        db.session.commit()

    def test_source_update_9(self):
        s = Subcommittee(name="National Security Department")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Subcommittee).filter_by(name = "National Security Department").one()
        r.name = "Western Department in National Security"
        self.assertEqual(str(r.name), "Western Department in National Security")

        db.session.query(Subcommittee).filter_by(name = "Western Department in National Security").delete()
        db.session.commit()

    def test_source_update_10(self):
        s = Hearing(date="1930/1/1", committee_id="EFGH", time="11:00:00", location="LG-000", description="Result")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Hearing).filter_by(date = "1930/1/1").one()
        r.time = "13:00:00"
        self.assertEqual(str(r.time), "13:00:00")

        db.session.query(Hearing).filter_by(date = "1930/1/1").delete()
        db.session.commit()

        db.session.query(Committee).filter_by(id = "EFGH").delete()

    def test_source_update_11(self):
        # preprocess clean-up
        db.session.query(Member).filter_by(id = "678").delete()
        db.session.commit()
        db.session.query(Legislation).filter_by(bill_id = "456").delete()
        db.session.commit()
        
        s = Member(id="678", fname="Mr", lname="Bean", mname="L", namesuffix="Jr.", party="party1", state="state1", state_rank="rank1", phone="5121234567", mailing_address="123 St", votes_w_party=95, votes_against_party=5, url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        s = Legislation(bill_id="456", cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", sponsor_id="678", bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        s = Action(action_id="100", bill_id="456", date="1990/11/1", description="passed")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Action).filter_by(action_id = "100").one()
        r.description = "veto"
        self.assertEqual(str(r.description), "veto")

        db.session.query(Action).filter_by(action_id = "100").delete()
        db.session.commit()

        db.session.query(Legislation).filter_by(bill_id = "456").delete()
        db.session.commit()

        db.session.query(Member).filter_by(id = "678").delete()
        db.session.commit()

if __name__ == '__main__':
    unittest.main()

# end of code
