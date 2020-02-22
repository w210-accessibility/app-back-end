from flask import Flask
from flask import request, jsonify
from ClientPrediction import ClientPrediction
from flask_cors import CORS

# EB looks for an 'application' callable by default.
application = Flask(__name__)
CORS(application)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: '<h1>Hi</h1>'))

# add a rule when the page is accessed with a name appended to the site
# URL.
@application.route('/api/predictions/', methods=['GET'])
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

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
