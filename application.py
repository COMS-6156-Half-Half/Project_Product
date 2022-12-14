from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL


from backend.models import db, Products
from backend.add_product import add_product
from backend.get_product import get_product
from backend.search_product import search_product
from backend.search_ptype import search_ptype
from backend.seller_product import seller_product


import flask_login
from datetime import datetime

# for image uploading
import os, base64

application = Flask(__name__)
# mysql = MySQL()
application.secret_key = 'super secret string'  # Change this!

UPLOAD_FOLDER = 'static/uploads/'

application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
application.config['SQLALCHEMY_DATABASE_URI'] ="mysql+pymysql://root:13886003474cjw@e61561.cwsqeuuovxq1.us-east-1.rds.amazonaws.com:3306/product"
db.init_app(application)
application.app_context().push()

application.register_blueprint(add_product)
application.register_blueprint(search_product)#if error: AttributeError:'function' object has no attribute 'register'
application.register_blueprint(search_ptype)#change the function name inside .py file: function name cannot have same name as Blueprint name
# application.register_blueprint(get_all_products)
# application.register_blueprint(show)
application.register_blueprint(get_product)
application.register_blueprint(seller_product)




@application.route('/')
def index():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8000)
