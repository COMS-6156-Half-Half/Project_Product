from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary

db = SQLAlchemy()

class Products(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100))
    description = db.Column(db.String(255))
    location = db.Column(db.String(100))
    price = db.Column(db.Integer)
    ptype = db.Column(db.String(100))
    retailer_link = db.Column(db.String(500))
    seller_id = db.Column(db.Integer)
    # image = db.Column(LargeBinary(length=(2**32)-1))
    sold = db.Column(db.Boolean, default=False)
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
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
