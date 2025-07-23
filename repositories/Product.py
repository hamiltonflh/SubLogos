from repositories.database import db

class Product(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)