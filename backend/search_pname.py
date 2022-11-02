from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from backend.models import db, Products

search_pname = Blueprint('search_pname', __name__, template_folder='../frontend')


@search_pname.route('/search_product/<pname>')
def search_product(pname):
    if pname == "all":
        product_list = Products.query.all()
        print(product_list)
        return render_template('search_pname.html', product_list=product_list, pname="all products on sale")
    pname = pname.lower()
    product_list = Products.query.filter_by(pname=pname).all()
    print("search for", pname, "in db:", product_list)

    return render_template('search_pname.html', product_list=product_list, pname=pname)
