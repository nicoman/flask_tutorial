from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Add config file
app.config.from_object('config')

# Define db object
db = SQLAlchemy(app)

from app import views, models
