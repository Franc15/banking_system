import os
from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'bank_test' # edit here
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
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    dob = Column(Date)
    password = Column(String)
    email = Column(String)
    accounts = db.relationship('Account', backref='account_owner')


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
            'id': self.id
        }

class Account(db.Model):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    accNo = Column(String)
    balance = Column(Integer)
    user_id = Column(Integer, db.ForeignKey('user.id'), nullable=False)
    accType_id = Column(Integer, db.ForeignKey('account_type.id'), nullable=False)

    # def __init__(self, accNo, accType, balance, user):
    #     self.accNo = accNo
    #     self.accType = accType
    #     self.balance = balance
    #     self.user = user

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
            'accNo': self.accNo,
            'accType': self.accType,
            'balance': self.balance,
            'user_id': self.user
        }

class AccountType(db.Model):
    __tablename__ = 'account_type'

    id = Column(Integer, primary_key=True)
    accType = Column(String)
    accounts = db.relationship('Account', backref='account_type')

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
            'accType': self.accType
        }
