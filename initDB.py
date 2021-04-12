from flask_migrate import Migrate, MigrateCommand

from App.main import app
from App.models.database import db

db.create_all(app=app)
print('Database intialized!')