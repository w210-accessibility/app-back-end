from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from mvp_endpoint.ClientPrediction import *
from mvp_endpoint import db
from mvp_endpoint.models import Pano, PanoFeature, SidewalkSegment2, SidewalkSegment3, SegmentToPano2
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
    sw_lat = try_parse_float(request.args.get('lat1'))
    sw_long = try_parse_float(request.args.get('long1'))
    ne_lat = try_parse_float(request.args.get('lat2'))
    ne_long = try_parse_float(request.args.get('long2'))

    passable_results = SidewalkSegment3.query.filter(SidewalkSegment3.startLat >= sw_lat) \
                                             .filter(SidewalkSegment3.startLat <= ne_lat) \
                                             .filter(SidewalkSegment3.startLong >= sw_long) \
                                             .filter(SidewalkSegment3.startLong <= ne_long) \
                                             .filter(SidewalkSegment3.roadGrade <= .05) \
                                             .all()

    part_passable_results = SidewalkSegment3.query.filter(SidewalkSegment3.startLat >= sw_lat) \
                                                  .filter(SidewalkSegment3.startLat <= ne_lat) \
                                                  .filter(SidewalkSegment3.startLong >= sw_long) \
                                                  .filter(SidewalkSegment3.startLong <= ne_long) \
                                                  .filter(SidewalkSegment3.roadGrade >= .05) \
                                                  .filter(SidewalkSegment3.roadGrade <= .1) \
                                                  .all()

    impassable_results = SidewalkSegment3.query.filter(SidewalkSegment3.startLat >= sw_lat) \
                                                .filter(SidewalkSegment3.startLat <= ne_lat) \
                                                .filter(SidewalkSegment3.startLong >= sw_long) \
                                                .filter(SidewalkSegment3.startLong <= ne_long) \
                                                .filter(SidewalkSegment3.roadGrade >= .1) \
                                                .all()

    response_geojson = {}
    passable_sidewalks = [res.geoJson for res in passable_results]
    part_passable_sidewalks = [res.geoJson for res in part_passable_results]
    impassable_sidewalks = [res.geoJson for res in impassable_results]

    # TODO change missing/issues language to reflect "passability" scheme
    response_geojson["passable_sidewalks"] = passable_sidewalks
    response_geojson["missing_sidewalk"] = part_passable_sidewalks
    response_geojson["sidewalk_issues"] = impassable_sidewalks
    return jsonify(response_geojson)

def try_parse_float(inp):
    try:
        x = float(inp)
    except:
        x = 0
    return x
