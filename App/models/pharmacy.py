from .database import db

#Not in use yet as Pharmacy info can't be updated from CRM yet.
class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(20), nullable=False)