from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
import json
from backend.models import db, Products
import base64

get_product = Blueprint('get_product', __name__, template_folder='../frontend')


@get_product.route('/get_product/<pid>', methods=['GET', 'POST'])
def show(pid):
  # print('====== pid ======')
  # print(pid)

  if request.method == 'GET':
    # check pid in db
    prod = Products.query.filter_by(pid=pid).first()
    # print(prod.pname)
    if prod == None:
      return Response("Sorry the product with pid= " + pid + " doesn't exist", status=404, content_type="text/plain")
    # try:
    #     image = prod.image.decode('ascii')
    # except:
    #     image = None
    result = {
      "data": [{
        # "prod": prod,
        "pname": prod.pname,
        "pid": prod.pid,
        "description": prod.description,
        "location": prod.location,
        "price": prod.price,
        "ptype": prod.ptype,
        "retailer_link": prod.retailer_link,
        "sold": prod.sold,
        "seller_id": prod.seller_id,
      }],
      "links": [{"rel": "self", "href": "/get_product/" + str(prod.pid)},
                {"rel": "type", "href": "/search_ptype/" + prod.ptype}]

    }

    # return render_template('get_product.html', pid=pid, prod = prod, image = image)
    return Response(json.dumps(result), status=200, content_type="application/json")
  else:
    prod = Products.query.filter_by(pid=pid).first()
    if not prod:
      return Response("Failed: Product NOT FOUND", status=404, content_type="text/plain")
    else:
      data = request.get_json()
      type = data['type']
      if type == 'delete':
        print('start deleting the product:', prod)
        db.session.delete(prod)
        db.session.commit()
        print('success delete')
        return Response("Product successfully deleted", status=200, content_type="text/plain")
      elif type == 'purchase':
        print('start purchasing the product: ', prod)
        prod.sold = True
        db.session.commit()
        print('success purchase')
        return Response("Product successfully purchased(sold=True)", status=200, content_type="text/plain")

  # return str(product_detail[0])
