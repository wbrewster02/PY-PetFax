from flask import ( Blueprint, render_template ) 
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")

# @bp.route('/facts')
# def factoids(): 
#     return render_template('new.html')

@bp.route('/new')
def new(): 
    return render_template('new.html')