from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from backend.models import db, Products

search_ptype = Blueprint('search_ptype', __name__, template_folder='../frontend')


@search_ptype.route('/search_ptype/<ptype>')
def search_product(ptype):
    product_list = Products.query.filter_by(ptype=ptype).all()
    print("search for", ptype, "in db:", product_list)

    return render_template('search_ptype.html', product_list=product_list, ptype=ptype)
