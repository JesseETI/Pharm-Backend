import json, os

CONFIG = None

environment = os.environ.get('ENV')
if environment is None:
    environment = 'staging'
    with open('environment.'+environment+'.json') as config_file:
        CONFIG = json.load(config_file)
else:
    #configuration for local environment
    CONFIG = {
        "dbtype": os.environ.get('DBTYPE'),
        "dbhost" : os.environ.get('DBHOST'),
        "debug" : True,
        "JWTdeltaDays": 7,
        "uploadDir":"App/uploads/",
        "dbname" : os.environ.get('DBNAME'),
        "dbuser" : os.environ.get('DBUSER'),
        "secret_key" : os.environ.get('SECRET_KEY'),
        "dbpassword": os.environ.get('DBPASSWORD'),
        "dbport" : os.environ.get('DBPORT'),
        #Google Firebase
        "apiKey": os.environ.get("API_KEY"),
        "authDomain": os.environ.get("AUTH_DOMAIN"),
        "databaseURL": os.environ.get("DATABASE_URL"),
        "projectId": os.environ.get("PROJECT_ID"),
        "storageBucket": os.environ.get("STORGAGE_BUCKET"),
        "messagingSenderId": os.environ.get("MESSAGING_SENDER_ID"),
        "appId": os.environ.get("APP_ID"),
        "measurementId" : os.environ.get("MEASUREMENT_ID")
    }
CONFIG['ENV']=environment