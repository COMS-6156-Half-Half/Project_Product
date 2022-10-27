from flask import Flask, Response, request, render_template, redirect, url_for
from flaskext.mysql import MySQL
# import pymysql
import flask_login
from datetime import datetime


#for image uploading
import os, base64
app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'super secret string'  # Change this!

#These will need to be changed according to your creditionals
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '13886003474cjw'
app.config['MYSQL_DATABASE_DB'] = 'Product'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


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
mysql.init_app(app)

#begin code used for login
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)

conn = mysql.connect()
# conn = _get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT email from Users")
# users = cursor.fetchall()


@app.route('/')
def hello_world():  # put application's code here

    return render_template('hello.html')

@app.route('/add_product', methods=['GET', 'POST'])
# @flask_login.login_required
def add_product():
    if request.method != 'POST':
        return render_template('add_product.html')

    pid = request.form.get('pid')
    description = request.form.get('description')
    price = request.form.get('price')

    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO PRODUCT (pid, description, price) VALUES (\'{pid}\', {description}, \'{price}\')')
    cursor.commit()
    return render_template('add_product.html')

@app.route('/search_product/<pname>')
def search_product(pname):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product WHERE  pname = '{0}'".format(pname))
    product_list = cursor.fetchall()

    return str(product_list)

@app.route('/get_product/<pid>')
def get_product(pid):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product WHERE pid = {0}".format(pid))
    product_detail = cursor.fetchall()

    return str(product_detail[0])

if __name__ == '__main__':
    app.run()
