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
    }
CONFIG['ENV']=environment