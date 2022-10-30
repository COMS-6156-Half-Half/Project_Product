from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from models import db, Products
search_pname = Blueprint('search_pname', __name__, template_folder='../frontend')

@search_pname.route('/search_product/<pname>')
def search_product(pname):
    pname = pname.lower()
    product_list = Products.query.filter_by(pname=pname).all()
    print(product_list)
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM Product WHERE  pname = '{0}'".format(pname))
    # product_list = cursor.fetchall()

    return render_template('search_pname.html', product_list=product_list, pname=pname)