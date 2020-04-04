from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from mvp_endpoint.ClientPrediction import *
from mvp_endpoint import db
from mvp_endpoint.models import Pano, PanoFeature, SidewalkSegment2, SidewalkSegment3, SidewalkSegment4, SegmentToPano2, SegmentToPano3, InSituFeedback
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import math

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

    passable_results = SidewalkSegment4.query.filter(SidewalkSegment4.startLat >= sw_lat) \
                                             .filter(SidewalkSegment4.startLat <= ne_lat) \
                                             .filter(SidewalkSegment4.startLong >= sw_long) \
                                             .filter(SidewalkSegment4.startLong <= ne_long) \
                                             .filter(SidewalkSegment4.roadGrade <= .05) \
                                             .all()

    part_passable_results = SidewalkSegment4.query.filter(SidewalkSegment4.startLat >= sw_lat) \
                                                  .filter(SidewalkSegment4.startLat <= ne_lat) \
                                                  .filter(SidewalkSegment4.startLong >= sw_long) \
                                                  .filter(SidewalkSegment4.startLong <= ne_long) \
                                                  .filter(SidewalkSegment4.roadGrade >= .05) \
                                                  .filter(SidewalkSegment4.roadGrade <= .1) \
                                                  .all()

    impassable_results = SidewalkSegment4.query.filter(SidewalkSegment4.startLat >= sw_lat) \
                                                .filter(SidewalkSegment4.startLat <= ne_lat) \
                                                .filter(SidewalkSegment4.startLong >= sw_long) \
                                                .filter(SidewalkSegment4.startLong <= ne_long) \
                                                .filter(SidewalkSegment4.roadGrade >= .1) \
                                                .all()

    response_geojson = {}
    passable_sidewalks = [res.geoJson for res in passable_results]
    part_passable_sidewalks = [res.geoJson for res in part_passable_results]
    impassable_sidewalks = [res.geoJson for res in impassable_results]

    # TODO change missing/issues language to reflect "passability" scheme
    response_geojson["passable_sidewalks"] = passable_sidewalks
    response_geojson["missing_sidewalk"] = part_passable_sidewalks
    response_geojson["sidewalk_issues"] = impassable_sidewalks

    num_passable_chunks = math.ceil(len(passable_sidewalks) / 5000)
    for i in range(1, num_passable_chunks):
        end_idx = i*5000
        if end_idx > len(passable_sidewalks):
            end_idx = len(num_passable_chunks) + 1
        tileset_json = {"passable_sidewalks": passable_sidewalks[(i-1)*5000:end_idx]}
        with open('mar29_passable_data_{}.json'.format(i), 'w') as outfile:
            json.dump(tileset_json, outfile)
    with open('mar29_part_passable_data.json', 'w') as outfile:
        tileset_json = {"part_passable_sidewalks": part_passable_sidewalks}
        json.dump(tileset_json, outfile)
    with open('mar29_impassable_data.json', 'w') as outfile:
        tileset_json = {"impassable_sidewalks": impassable_sidewalks}
        json.dump(tileset_json, outfile)
    return jsonify(response_geojson)

def try_parse_float(inp):
    try:
        x = float(inp)
    except:
        x = 0
    return x

@bp.route('/api/addInSitu/', methods=['POST'])
def add_in_situ_feedback():
    status = False
    try:
        req = request.json;
        new_feedback = InSituFeedback(req['lat'], req['long'], req['mode'], req['label'])
        db.session.add(new_feedback)
        db.session.commit()
        status = True
    except:
        pass
    return {"db_success_indicator": status}

@bp.route('/api/getInSitu/', methods=['GET'])
def get_in_situ_feedback():
    response = {}
    # we can distinguish this query more if we want to have different symbols
    # for different things
    all_feedback = InSituFeedback.query.all()
    result_list = [{'location': [res.long, res.lat], 'label': res.label} for res in all_feedback]
    response['in_situ_results'] = result_list
    return jsonify(response)
