from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from mvp_endpoint.ClientPrediction import *
from mvp_endpoint import db
from mvp_endpoint.models import PointFeature
from flask import jsonify

bp = Blueprint('mvp_endpoint', __name__)

# add a rule for the index page.
@bp.route('/', methods=['Get'])
def index():
    return '<h1>Hi</h1>'

# add a rule when the page is accessed with a name appended to the site
# URL.
@bp.route('/api/predictions/', methods=['GET'])
def get_data_for_bounding_box():
    lat1 = try_parse_int(request.args.get('lat1'))
    long1 = try_parse_int(request.args.get('long1'))
    lat2 = try_parse_int(request.args.get('lat2'))
    long2 = try_parse_int(request.args.get('long2'))

    # PLACEHOLDER making a couple generic objects to pass back
    return_list = [ClientPrediction(lat1, long1, 0), ClientPrediction(lat2,long2,2)]

    return jsonify({'preds': [pred.to_dict() for pred in return_list]})

def try_parse_int(inp):
    try:
        x = int(inp)
    except:
        x = 0
    return x
