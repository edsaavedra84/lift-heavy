from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger(__name__)

logging.info('Starting App!')
app = Flask(__name__)

#TODO: remember parameters for mysql database!
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:secret@127.0.0.1:3306/lift_heavy?charset=utf8mb4'
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'pass.1234'

db = SQLAlchemy(app)
logging.info('App started!')  # will print a message to the console

import routes.GeneralRoutes