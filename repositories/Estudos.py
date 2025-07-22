from repositories.database import db

class Estudos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(), nullable=False)
    resume = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(), nullable=False)


