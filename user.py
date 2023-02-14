from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# from flask_app.__init__ import app
from flask_app import app
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.business_name = data['business_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.materials = []




    @classmethod
    def save_new_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, business_name) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, %(business_name)s);'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        print('here we go')
        return results


    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM users where email = %(email)s;'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        if len(results) <=0:
            return False
        return cls(results[0])

    
    @classmethod
    def get_password(cls, data):
        query = 'SELECT users.password FROM users WHERE email = %(email)s;'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        return results


    @classmethod
    def fetch_account_info(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        return cls(results[0])



    @classmethod
    def get_all(cls):
        query = 'SELECT * From users;'
        results = connectToMySQL('solo_project_4').query_db(query)
        print(results)
        return results



    @staticmethod
    def validate_new_user(user):
        is_valid = True
        
        if len(user['password']) < 8:
            flash('******Password must be at least 8 characters******')
            is_valid = False

        if user['confirm_password'] != user['password']:
            flash('******Passwords must be the same******')
            is_valid = False

        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('solo_project_4').query_db(query, user)

        if not EMAIL_REGEX.match(user['email']):
            flash('******Invalid email address******')
            is_valid = False

        if len(results) >= 1:
            flash('******There is already an account associated with that email address******')
            is_valid = False

        return is_valid