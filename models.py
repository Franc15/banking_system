import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'banking' # edit here
database_path = 'postgresql://{}/{}'.format('postgres:franc123@localhost:5432', database_name)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)
    dob = Column(Date)
    phone = Column(String)
    password = Column(String)
    country = Column(String)
    email = Column(String)
    empStat = Column(String)

    def __init__(self, fname, lname, gender, dob, phone, password, country, email, empStat):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.dob = dob
        self.phone = phone
        self.password = password
        self.country = country
        self.email = email
        self.empStat = empStat


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'gender': self.gender,
            'dob': self.dob,
            'phone': self.phone,
            'password': self.password,
            'country': self.country,
            'email': self.email
        }