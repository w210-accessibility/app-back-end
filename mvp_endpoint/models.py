from mvp_endpoint import db

# TODO figure out how to map label ints to actual labels
# switch to enum type? or make a type table?
class Pano(db.Model):
    panoId = db.Column(db.Text(), primary_key=True)
    headingDegree = db.Column(db.Float, primary_key=True)
    linearId = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

# this table probably doesn't actually need linearId,
# since we could get it from pano table, but might be helpful
# to have just to make query faster...
class PanoFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panoId = db.Column(db.Text(), nullable=False)
    linearId = db.Column(db.Integer, nullable=False)
    headingDegree = db.Column(db.Float, nullable=False)
    label = db.Column(db.Integer, nullable=False)
    source = db.Column(db.Text(), nullable=False)

# TODO: figure out elevation, geojson, sidewalk present indicator..
class SidewalkSegment(db.Model):
    linearId = db.Column(db.Integer, primary_key=True)
    directionInd = db.Column(db.Text(), primary_key=True)
    streetName = db.Column(db.Text(), nullable=True)
    startLat = db.Column(db.Float, nullable=False)
    startLong = db.Column(db.Float, nullable=False)
    endLat = db.Column(db.Float, nullable=False)
    endLong = db.Column(db.Float, nullable=False)
    geoJson = db.Column(db.JSON, nullable=False)
