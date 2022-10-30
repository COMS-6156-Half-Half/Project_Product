from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100))
    description = db.Column(db.String(255))
    price = db.Column(db.Float)

    # def __init__ (self, db.Model):
    #     pid = db.Column(db.Integer, primary_key = True)
    #     pname = db.Column(db.String(100))
    #     description =db.Column(db.String(255))
    #     price = db.Column(db.Float)
    #
    #     self.pid, self.pname, self.description, self.price = pid, pname, description, price
    #
    # def printALL():
    #     print('pid {0} | pname {1} | description {2} | price {3}')