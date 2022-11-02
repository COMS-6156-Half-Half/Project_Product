from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from backend.models import db, Products

search_box = Blueprint('search_box', __name__, template_folder='../frontend')


@search_box.route('/search', methods=['POST'])
def search_product():
    pname = request.form['pname']
    product_list = Products.query.filter_by(pname=pname).all()
    print("search for", pname, "in db:", product_list)

    return render_template('search_pname.html', product_list=product_list, pname=pname)
