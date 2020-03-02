from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from mvp_endpoint.ClientPrediction import *
from mvp_endpoint import db
from mvp_endpoint.models import Pano, PanoFeature, SidewalkSegment2
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('mvp_endpoint', __name__)

# add a rule for the index page.
@bp.route('/', methods=['Get'])
def index():
    return '<h1>Hi</h1>'

# add a rule when the page is accessed with a name appended to the site
# URL.
@bp.route('/api/predictions/', methods=['GET'])
def get_data_for_bounding_box():
    # for mapbox, bounding boxes go (SW, NE)
    sw_lat = try_parse_int(request.args.get('lat1'))
    sw_long = try_parse_int(request.args.get('long1'))
    ne_lat = try_parse_int(request.args.get('lat2'))
    ne_long = try_parse_int(request.args.get('long2'))

    results = SidewalkSegment2.query.filter(SidewalkSegment2.startLat >= sw_lat) \
                                    .filter(SidewalkSegment2.startLat <= ne_lat) \
                                    .filter(SidewalkSegment2.startLong <= sw_long) \
                                    .filter(SidewalkSegment2.startLong >= ne_long).all()

    # this is just a hacky little test
    # next I need to figure out if I need to combine all these into one featureCollection or not
    if len(results) == 0:
        result = {}
    else:
        result = results[0].geoJson
    return jsonify({"number of results": len(results),
                    "first geoJson": result})

def try_parse_int(inp):
    try:
        x = int(inp)
    except:
        x = 0
    return x
