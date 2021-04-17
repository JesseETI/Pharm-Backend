from flask import Flask
from flask_jwt import JWT
from flask import session
from datetime import timedelta 
from flask_cors import CORS
import pyrebase


from App.models.database import *

from App.models.user import *

from App.controllers.auth import *

from App import CONFIG

from App.views import (
    api_views,
    product_views,
    auth_views,
    search_view,
    order_views,
    customer_views
)

#Google Firebase configuration file.

'''
config = {
    "apiKey": CONFIG['apiKey'],
    "authDomain": CONFIG['authDomain'],
    "databaseURL": CONFIG['databaseURL'],
    "projectId": CONFIG['projectId'],
    "storageBucket": CONFIG['storageBucket'],
    "messagingSenderId": CONFIG['messagingSenderId'],
    "appId": CONFIG['appId'],
    "measurementId": CONFIG['measurementId'],
  }
'''

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

#to store image
#storage.child("image-url-on-firebase").put("image-name.jpg") (png whatever file extension")

#to download image
#storage.child("image-url-on-firebase").download("image-name.jpg")

def create_app():
    app = Flask(__name__, static_url_path='')
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://m0k7jdg650wjsxom:scq41zzt7ww7dwpf@grp6m5lz95d9exiz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/vsqto06i0kdvymfw'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SECRET_KEY'] = CONFIG['secret_key']
    app.config['UPLOADED_PHOTOS_DEST'] = CONFIG['uploadDir']
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=CONFIG['JWTdeltaDays'])
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
    #photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    #configure_uploads(app, photos)
    db.init_app(app)
    return app

app = create_app()

app.app_context().push()

app.register_blueprint(api_views)
app.register_blueprint(product_views)
app.register_blueprint(auth_views)
app.register_blueprint(search_view)
app.register_blueprint(order_views)
app.register_blueprint(customer_views)

jwt = JWT(app, authenticate, identity) 

if __name__ == '__main__':
    print('Application running in '+CONFIG['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=CONFIG['debug'])
