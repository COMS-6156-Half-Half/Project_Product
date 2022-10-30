from flask import Blueprint, url_for, render_template, redirect, request
import sqlalchemy
from models import db, Products

remove_product = Blueprint('add_product', __name__, template_folder='../frontend')
