from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
import json
from backend.models import db, Products

seller_product = Blueprint('seller_product', __name__, template_folder='../frontend')


# search_box = Blueprint('search_box', __name__, template_folder='../frontend')

@seller_product.route('/seller_product/<uid>', methods=['GET'])
def show(uid):
  product_list = Products.query.filter_by(seller_id=uid).all()
  result = []
  for prod in product_list:
    result.append(Products.as_dict(prod))
  return Response(json.dumps(result), status=200, content_type="application/json")
