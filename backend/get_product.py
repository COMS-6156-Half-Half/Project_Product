from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from models import db, Products
get_product = Blueprint('get_product', __name__, template_folder='../frontend')


@get_product.route('/get_product/<pid>', methods=['GET', 'POST'])
def show(pid):
    print('====== pid ======')
    print(pid)
    if request.method == 'GET':
        #check pid in db
        return render_template('get_product.html', pid=pid)
    else:
        value = request.form['distinction']

        print('-----')
        print(value)

        prod = Products.query.filter_by(pid = pid).first()

        if value == '1':
            print('start delete')
            db.session.delete(prod)
            db.session.commit()
            print('success delete')
            return render_template('index.html')
        elif value == '2':
            return

        prod = Products.query.filter_by(pid = pid)

    # return str(product_detail[0])