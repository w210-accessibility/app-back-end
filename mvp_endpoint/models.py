from mvp_endpoint import db
from sqlalchemy.sql import func


# TODO figure out how to map label ints to actual labels
# switch to enum type? or make a type table?
class Pano(db.Model):
    panoId = db.Column(db.String(length=50), primary_key=True)
    headingDegree = db.Column(db.Float, primary_key=True)
    linearId = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

# this table probably doesn't actually need linearId,
# since we could get it from pano table, but might be helpful
# to have just to make query faster...
class PanoFeature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panoId = db.Column(db.String(length=50))
    linearId = db.Column(db.Integer, nullable=False)
    headingDegree = db.Column(db.Float, nullable=False)
    label = db.Column(db.Integer, nullable=False)
    source = db.Column(db.Text(), nullable=False)

class SidewalkSegment2(db.Model):
    segmentId = db.Column(db.Integer, primary_key=True)
    directionInd = db.Column(db.String(length=50), primary_key=True)
    linearId = db.Column(db.Integer, nullable=False)
    streetName = db.Column(db.Text(), nullable=True)
    startLat = db.Column(db.Float, nullable=False)
    startLong = db.Column(db.Float, nullable=False)
    endLat = db.Column(db.Float, nullable=False)
    endLong = db.Column(db.Float, nullable=False)
    whichArcgisFile = db.Column(db.String(length=10))
    geoJson = db.Column(db.JSON, nullable=False)

class SidewalkSegment3(db.Model):
    segmentId = db.Column(db.Integer, primary_key=True)
    directionInd = db.Column(db.String(length=50), primary_key=True)
    linearId = db.Column(db.Integer, nullable=False)
    streetName = db.Column(db.Text(), nullable=True)
    startLat = db.Column(db.Float, nullable=False)
    startLong = db.Column(db.Float, nullable=False)
    endLat = db.Column(db.Float, nullable=False)
    endLong = db.Column(db.Float, nullable=False)
    whichArcgisFile = db.Column(db.String(length=10))
    roadGrade = db.Column(db.Float, nullable=False)
    geoJson = db.Column(db.JSON, nullable=False)
    updateTs = db.Column(db.DateTime(), server_default=func.now())

# TODO: maybe we won't use this at all and just go with my original idea
class SegmentToPano2(db.Model):
    linkId = db.Column(db.Integer, primary_key=True)
    segmentId = db.Column(db.Integer, db.ForeignKey(SidewalkSegment2.segmentId))
    panoId = db.Column(db.Integer)
    headingDegree = db.Column(db.Float)
