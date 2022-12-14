from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
import json
from backend.models import db, Products

search_ptype = Blueprint('search_ptype', __name__, template_folder='../frontend')


@search_ptype.route('/search_ptype/<ptype>')
def search_product(ptype):
    product_list = Products.query.filter_by(ptype=ptype).all()
    print("search for", ptype, "in db:", product_list)

    # return render_template('search_ptype.html', product_list=product_list, ptype=ptype)
    result = []
    for prod in product_list:
      result.append(Products.as_dict(prod))

    # return render_template('search_pname.html', product_list=product_list, pname=pname)
    if result == [] or len(result) == 0:
      return Response("Current product type: NOT FOUND", status = 404, content_type="text/plain")
    else:
      return Response(json.dumps(result), status=200, content_type="application/json")

