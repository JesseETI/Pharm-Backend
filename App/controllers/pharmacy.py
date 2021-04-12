from App.models import Pharmacy
from App.models.database import db

def create_pharmacy(name, address, contact):
    newPharm = Pharmacy(name = name, address = address, contact = contact)
    db.session.add(newPharm)
    db.session.commit()
    return newPharm