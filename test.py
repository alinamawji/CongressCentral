#!/usr/bin/env python3

# -------
# imports
# -------

import os
import sys
import unittest
from models import db, Committee, Member, Legislation

# -----------
# DBTestCases
# -----------
class DBTestCases(unittest.TestCase):
    # ---------
    # insertion
    # ---------

    def test_source_insert_1(self):
        s = Committee(name="committee1", website="https://www.committee1.com/", branch="senate", chair_id=1234, ranking_id=5678)
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Committee).filter_by(name = "committee1").one()
        self.assertEqual(str(r.name), "committee1")

        db.session.query(Committee).filter_by(name = "committee1").delete()
        db.session.commit()

    def test_source_insert_2(self):
        s = Member(id=987, Fname="Mr", Lname="Bean", MI="L", suffix="Jr.", party="party1", state="state1", state_rank="rank1", phone=5121234567, mailing_address="123 St", votes_w_party=95, votes_ag_party="5", url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Member).filter_by(id = 987).one()
        self.assertEqual(str(r.id), 987)

        db.session.query(Member).filter_by(id = 987).delete()
        db.session.commit()

    def test_source_insert_3(self):
        s = Legislation(bill_id=123, cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", member_id=678, bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Legislation).filter_by(bill_id = 123).one()
        self.assertEqual(str(r.bill_id), 123)

        db.session.query(Legislation).filter_by(bill_id = 123).delete()
        db.session.commit()

    def test_source_update_1(self):
        s = Committees(name="committee1", website="https://www.committee1.com/", branch="senate", chair_id=1234, ranking_id=5678)
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Committee).filter_by(name = "committee1").one()
        r.branch = "house"
        self.assertEqual(str(r.branch), "house")

        db.session.query(Committee).filter_by(name = "committee1").delete()
        db.session.commit()

    def test_source_insert_2(self):
        s = Members(id=987, Fname="Mr", Lname="Bean", MI="L", suffix="Jr.", party="party1", state="state1", state_rank="rank1", phone=5121234567, mailing_address="123 St", votes_w_party=95, votes_ag_party="5", url="https://mrbean.com/")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Member).filter_by(id = 987).one()
        r.party = "party2"
        self.assertEqual(str(r.party), "party2")

        db.session.query(Member).filter_by(id = 987).delete()
        db.session.commit()

    def test_source_insert_3(self):
        s = Legislation(bill_id=123, cosponsors=3, summary="A bill about bills.", type="Resolution", date_introduced="01/01/2021", member_id=678, bill_number="Res. 123")
        db.session.add(s)
        db.session.commit()

        r = db.session.query(Legislation).filter_by(bill_id = 123).one()
        r.cosponsors = 5
        self.assertEqual(str(r.cosponsors), 5)

        db.session.query(Legislation).filter_by(bill_id = 123).delete()
        db.session.commit()

if __name__ == '__main__':
    unittest.main()

# end of code
