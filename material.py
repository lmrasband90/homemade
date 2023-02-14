from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.__init__ import app



class Material:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.category = data['category']
        self.supplier = data['supplier']
        self.in_stock = data['in_stock']
        self.alert_amount = data['alert_amount']
        self.unit_of_measure = data['unit_of_measure']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = None





    @classmethod
    def get_all_materials(cls):
        query = 'SELECT * FROM materials'
        results = connectToMySQL('solo_project_4').query_db(query)
        return results


    @classmethod
    def get_one_material(cls, data):
        query = 'SELECT * FROM materials WHERE id = %(id)s'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        return cls(results[0])




    @classmethod
    def add_new_material(cls, data):
        query = 'INSERT INTO materials (name, category, supplier, in_stock, alert_amount, unit_of_measure, created_at, updated_at, user_id) VALUES ( %(name)s, %(category)s, %(supplier)s, %(in_stock)s, %(alert_amount)s, %(unit_of_measure)s, NOW(), NOW(), %(user_id)s );'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        print(results)
        return results


    @classmethod
    def update_material(cls, data):
        query = 'UPDATE materials SET name = %(name)s, category = %(category)s, supplier = %(supplier)s, alert_amount = %(alert_amount)s, in_stock = %(in_stock)s, unit_of_measure = %(unit_of_measure)s, updated_at = NOW() WHERE id = %(id)s;'
        results = connectToMySQL('solo_project_4').query_db(query, data)
        return results


    @classmethod
    def delete_material(cls, data):
        query = 'DELETE FROM materials WHERE id = %(id)s; '
        results = connectToMySQL('solo_project_4').query_db(query, data)
        return results


    @staticmethod
    def send_alert(material):
        if material['in_stock'] < 20:
            flash('******* You are running low **********')



