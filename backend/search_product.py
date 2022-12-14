from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
import json
from backend.models import db, Products

search_product = Blueprint('search_product', __name__, template_folder='../frontend')


# search_box = Blueprint('search_box', __name__, template_folder='../frontend')

@search_product.route('/search', methods=['POST'])
def search_box():
  data = request.get_json()
  pname = data['pname'].lower().strip()
  # product_list = Products.query.filter_by(pname=pname).all()
  product_list = Products.query.filter(Products.pname.contains(pname)).all()
  result = []
  for prod in product_list:
    result.append(Products.as_dict(prod))

  # return render_template('search_pname.html', product_list=product_list, pname=pname)
  if result == [] or len(result) == 0:
    return Response("Product you're searching: NOT FOUND", status = 404, content_type="text/plain")
  else:
    return Response(json.dumps(result), status=200, content_type="application/json")


@search_product.route('/search_product/', methods=['GET'])
@search_product.route('/search_product', methods=['GET'])
def get_all_product():
  product_list = Products.query.all()
  result = []
  for prod in product_list:
    result.append(Products.as_dict(prod))

  if result == [] or len(result) == 0:
    return Response("There is no product on sale.", status = 404, content_type="text/plain")
  else:
    return Response(json.dumps(result), status=200, content_type="application/json")
  # return render_template('search_pname.html', product_list=product_list, pname="all products on sale")


@search_product.route('/search_product/<pname>')
def search_by_name(pname):
  pname = pname.lower().strip()
  product_list = Products.query.filter_by(Products.pname.contains(pname)).all()
  result = []
  for prod in product_list:
    result.append(Products.as_dict(prod))

  # return render_template('search_pname.html', product_list=product_list, pname=pname)
  if result == [] or len(result) == 0:
    return Response("Product you're searching: NOT FOUND", status = 404, content_type="text/plain")
  else:
    return Response(json.dumps(result), status=200, content_type="application/json")
