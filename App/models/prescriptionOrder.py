#Not in use yet as no perscription order upload feature is available for project scope
from datetime import datetime
from .database import db
from .order import Order

class PrescriptionOrder(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(300), nullable=False)

    def createPrescriptionOrder():
        return ""

    def toDict(self):
        return ""

