import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, User, Account, AccountType


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()
    # setup_db(app)

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return 'Hello, World!'

    # @app.route('/register', methods=['POST'])
    # def user_register():
    #     # get user details 
    #     body = request.get_json()
    #     name = body.get('name', None)
    #     gender = body.get('gender', None)
    #     dob = body.get('dob', None)
    #     email = body.get('email', None)
    #     password = body.get('password', None)
    #     accType = body.get('accType', None)
    #     # create new user object
    #     user = User(name=name
    #                 , gender=gender
    #                 , dob=dob
    #                 , email=email
    #                 , password=password
    #                 )
    #     # create new account type object
    #     acc_type = AccountType.query.filter(AccountType.accType == accType).one_or_none()

    #     # create new account object
    #     account = Account(accNo=random.randint(1000000000, 9999999999)
    #                     , balance=0
    #                     , account_owner=user
    #                     , account_type=acc_type
    #                     )


    #     # add user to db 
    #     user.insert()
    #     # add account to db
    #     account.insert()

    #     # return the user as json
    #     return jsonify({
    #         'success': True,
    #         'data': user.format()
    #     })




    return app