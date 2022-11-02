from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL


from backend.models import db, Products
from backend.add_product import add_product
from backend.get_product import get_product
from backend.search_pname import search_pname
from backend.search_ptype import search_ptype
from backend.search_box import search_box

import flask_login
from datetime import datetime

# for image uploading
import os, base64

application = Flask(__name__)
# mysql = MySQL()
application.secret_key = 'super secret string'  # Change this!


application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../backend/database.db"
db.init_app(application)
application.app_context().push()

application.register_blueprint(add_product)
application.register_blueprint(search_pname)#if error: AttributeError:'function' object has no attribute 'register'
application.register_blueprint(search_ptype)#change the function name inside .py file: function name cannot have same name as Blueprint name
# application.register_blueprint(get_all_products)
# application.register_blueprint(show)
application.register_blueprint(get_product)
application.register_blueprint(search_box)



@application.route('/')
def index():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8000)
