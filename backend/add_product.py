import os.path

import flask_login
from flask import Blueprint, url_for, render_template, redirect, request, Response
import sqlalchemy
from backend.models import db, Products

import base64

add_product = Blueprint('add_product', __name__, template_folder='../frontend')

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# @flask_login.login_required
@add_product.route('/add_product', methods=['GET', 'POST'])
# @flask_login.login_required
def show():
    if request.method == 'GET':
        return render_template('add_product.html')
    else:
      data = request.get_json()
      description = data['description']
      price = int(data['price'])
      pname = data['pname'].lower().strip()
      ptype = data['ptype']
      location = data['location']
      seller_id = data['seller_id']
      retailer_link = data['retailer_link']

      # description = request.form['description']
      # price = int(request.form['price'])
      # pname = request.form['pname'].lower().strip()
      # ptype = request.form['ptype']
      # location = request.form['location']
      # # seller_id = flask_login.current_user.id
      # print("ptype is:", ptype)
      # retailer_link = request.form['retailer_link']

      # img_file = request.files['image']
      # img_file = base64.b64encode(img_file.read())

      # print(img_file.size)
      #
      # try:
      #     print(request.files['image'].filename)
      #     img_file = request.files['image']
      #     if img_file:
      #         print('received image')
      # except:
      #     img_file = None
      #     print('image failed')

      # print("retailer link is:", retailer_link)
      if price <= 0:
          # return render_template('add_product.html', success=False, message="Price should be at least $1.")
          return Response("Price should be at least $1.", status=400, content_type="text/plain")
      if ptype and price and pname:
          try:
              new_product = Products(
                  description=description,
                  price=price,
                  pname=pname,
                  ptype=ptype,
                  location=location,
                  retailer_link=retailer_link,
                  # image = img_file,
                  seller_id = seller_id
              )
              db.session.add(new_product)
              db.session.commit()
          except sqlalchemy.exc.IntegrityError:
            return Response("pid already existed", status=400, content_type="text/plain")
              # return redirect(url_for('add_product.show') + '?error=pid-exists')

          # can add a flash notice of "successfully add" on the page

          # return render_template('add_product.html', success=True)
          return Response("Product successfully added", status=200, content_type="text/plain")
      else:
          # return redirect(url_for('add_product.show') + '?success=missing-fields')
          return Response("Missing fields", status=400, content_type="text/plain")
