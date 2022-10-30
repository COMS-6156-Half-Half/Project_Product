from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
from models import db, Products
from add_product import add_product
from get_product import get_product
from search_pname import search_pname
import hello
# import pymysql
import flask_login
from datetime import datetime

# for image uploading
import os, base64

app = Flask(__name__)
# mysql = MySQL()
app.secret_key = 'super secret string'  # Change this!

# These will need to be changed according to your creditionals
# pp.config['MYSQL_DATABASE_USER'] = 'root'
# a.config['MYSQL_DATABASE_PASSWORD'] = '13886003474cjw'
# apponfig['MYSQL_DATABASE_DB'] = 'Product'
# app.cfig['MYSQL_DATABASE_HOST'] = 'localhost'

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:13886003474cjw@localhost/Product?host=localhost?port=3306"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../database.db"
db.init_app(app)
app.app_context().push()

app.register_blueprint(add_product)
app.register_blueprint(search_pname)
app.register_blueprint(get_product)
# app.register_blueprint(hello)


# def _get_connection():
#     usr = os.environ.get("dbuser")
#     pw = os.environ.get("dbpwd")
#     host = "e61561.cwsqeuuovxq1.us-east-1.rds.amazonaws.com"
#
#     conn = pymysql.connect(
#         user='root',
#         password='13886003474',
#         host='localhost',
#         cursorclass=pymysql.cursors.DictCursor,
#         autocommit=True
#     )
#     return conn
# mysql.init_app(app)

# begin code used for login
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)

# conn = mysql.connect()


# conn = _get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT email from Users")
# users = cursor.fetchall()


@app.route('/')
def index():  # put application's code here

    return render_template('index.html')







if __name__ == '__main__':
    app.run()
