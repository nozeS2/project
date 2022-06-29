from homepage import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sectors = db.Column(db.String(150), nullable=False)
    salery = db.Column(db.Integer, nullable = False)
    region = db.Column(db.String(200), nullable = False)
