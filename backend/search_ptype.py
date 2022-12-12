from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
import json
from backend.models import db, Products

search_ptype = Blueprint('search_ptype', __name__, template_folder='../frontend')

class BytesEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, bytes):
      return obj.decode('utf-8')
    return json.JSONEncoder.default(self, obj)


@search_ptype.route('/search_ptype/<ptype>')
def search_product(ptype):
    product_list = Products.query.filter_by(ptype=ptype).all()
    print("search for", ptype, "in db:", product_list)

    # return render_template('search_ptype.html', product_list=product_list, ptype=ptype)
    result = []
    for prod in product_list:
      result.append(Products.as_dict(prod))

    # return render_template('search_pname.html', product_list=product_list, pname=pname)
    return Response(json.dumps(result, cls=BytesEncoder), status=200, content_type="application/json")

