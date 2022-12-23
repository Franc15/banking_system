import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, User


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.app_context().push()
    setup_db(app)

    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/register', methods=['POST'])
    def user_register():
        # get user details 
        body = request.get_json()
        name = body.get('name', None)
        gender = body.get('gender', None)
        dob = body.get('dob', None)
        email = body.get('email', None)
        password = body.get('password', None)
        # create new user object
        user = User(name=name
                    , gender=gender
                    , dob=dob
                    , email=email
                    , password=password
                    )

        # add user to db 
        user.insert()
        # return the user as json
        return jsonify({
            'success': True,
            'data': user.format()
        })




    return app