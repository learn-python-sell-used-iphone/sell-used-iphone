from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Phone(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        actual_price = db.Column(db.Integer, nullable=False)
        text = db.Column(db.Text, nullable=True)
