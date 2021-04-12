#Not in use yet as payment is not a feature available for project scope
from datetime import datetime
from .database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    amount_paid = db.Column(db.Integer, nullable=False)
    date_paid = db.Column(db.DateTime(), nullable=False)
    
    def toDict(self):
        return {
            "id": self.id,
            "status": self.status,
            "amount_paid": self.amount_paid,
            "date_paid": self.date_paid
        }
