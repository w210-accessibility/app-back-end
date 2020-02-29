from mvp_endpoint import db

# TODO figure out how to map label ints to actual labels
# switch to anume type? or make a type table?
class PointFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panoId = db.Column(db.Text(), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    roadId = db.Column(db.Integer, nullable=False)
    label = db.Column(db.Integer, nullable=False)
    source = db.Column(db.Text(), nullable=False)

# TODO: figure out elevation, geojson, sidewalk present indicator..
# class SidewalkSegment(db.Model):
#     roadId = db.Column(db.Integer, primary_key=True)
#     directionInd = db.Column(db.Text(), primary_key=True)
#     startLat = db.Column(db.Float, nullable=False)
#     startLong = db.Column(db.Float, nullable=False)
#     endLat = db.Column(db.Float, nullable=False)
#     endLong = db.Column(db.Float, nullable=False)
#     geoJson = db.Column(db.JSON, nullable=False)
