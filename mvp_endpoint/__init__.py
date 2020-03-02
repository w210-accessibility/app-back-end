from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
import json
from flask import Flask
from flask import request
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    application = Flask(__name__)
    CORS(application)

    migrate = Migrate()

    if 'RDS_HOSTNAME' in os.environ:
          DATABASE = {
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
          }
          database_url = 'mysql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASE
    else:
        with open('dbconfig.json') as json_file:
            config = json.load(json_file)
        # TODO do not push this
        DATABASE = {
          'NAME': 'ebdb',
          'USER': config['DB_USER'],
          'PASSWORD': config['DB_PASSWORD'],
          'HOST': 'aa6f8tcntjfd0z.c5625ddefrth.us-west-2.rds.amazonaws.com',
          'PORT': 3306,
        }
        database_url = 'mysql+pymysql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASE
        #database_url = 'sqlite:///development.db'

    application.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = database_url,
        SQLALCHEMY_POOL_RECYCLE = 280,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(application)
    migrate.init_app(application, db)


    from . import models
    from . import mvp_endpoint
    application.register_blueprint(mvp_endpoint.bp)

    return application
