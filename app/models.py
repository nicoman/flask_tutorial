from app import db

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
