from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from backend.models import db, Products

add_product = Blueprint('add_product', __name__, template_folder='../frontend')


@add_product.route('/add_product', methods=['GET', 'POST'])
# @flask_login.login_required
def show():
    if request.method != 'POST':
        return render_template('add_product.html')
    # photo = request.form['photo']
    description = request.form['description']
    price = int(request.form['price'])
    pname = request.form['pname'].lower()
    ptype = request.form['ptype']
    location = request.form['location']
    print("ptype is:", ptype)
    retailer_link = request.form['retailer_link']
    print("retailer link is:", retailer_link)
    if price <= 0:
        return render_template('add_product.html', success=False, message="Price should be at least $1.")

    if ptype and price and pname:
        try:
            new_product = Products(
                # photo = photo,
                description=description,
                price=price,
                pname=pname,
                ptype=ptype,
                location=location,
                retailer_link=retailer_link
            )
            db.session.add(new_product)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect(url_for('add_product.show') + '?error=pid-exists')
        # can add a flash notice of "successfully add" on the page
        return render_template('add_product.html', success=True)
    else:
        return redirect(url_for('add_product.show') + '?success=missing-fields')
