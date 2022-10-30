from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from models import db, Products
add_product = Blueprint('add_product', __name__, template_folder='../frontend')

@add_product.route('/add_product', methods=['GET', 'POST'])
# @flask_login.login_required
def show():
    if request.method != 'POST':
        return render_template('add_product.html')
    # photo = request.form['photo']
    description = request.form['description']
    price = request.form['price']
    pname = request.form['pname'].lower()

    if description and price and pname:
        try:
            new_product = Products(
                # photo = photo,
                description = description,
                price = price,
                pname = pname,
            )
            db.session.add(new_product)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect(url_for('add_product.show') + '?error=pid-exists')
        #can add a flash notice of "successfully add" on the page
        return redirect(url_for('add_product.show') + '?success=product_added')
    else:
        return redirect(url_for('add_product.show') + '?success=missing-fields')

