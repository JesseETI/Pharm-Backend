
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#env=staging/https://github.com/uwidcit/pharm-backend)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Pharm Backend
Backend application for pharmacy application

# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```
$ pip3 install -r requirements.txt
```

# Running the Project
Ensure the environment varable ENV is either set to 'staging' or 'production' then execute the following command

_For development:_
```
$ python3 -m App.main
```
_For production using gunicorn:_
```
$ gunicorn -w 4 wsgi:app
```

# Deploying
App will be configured to auto deploy master branch to heroku at [https://uwipharm.herokuapp.com](https://uwipharm.herokuapp.com)

# Manage.py Commands

Manage.py is a utility script for performing various tasks related to the project. You can use it to import and test any code in the project. 
You just need create a manager command function, for example:

```
# inside manage.py


@manager.command
def hello():
    print('hello')

...    
```

Then execute the command by calling the funciton name as a parameter to the script

```
$ python3 manage.py hello
```

# Intializing the Database
When connecting the project to a fresh empty database ensure the appropriate database credentials are set in environment.staging.json file then run the following command.

When adding new models or changing models this command may also work. If it is unsuccessful you should use the migration command in the next section.

```
$ python3 manage.py initDB
```

# Database Migrations
If changes to the models are made, the database must be'migrated' so that it can be synced with the new models.
Then execute following commands using manage.py. More info [here](https://flask-migrate.readthedocs.io/en/latest/)

```
$ python3 manage.py db init
$ python3 manage.py db migrate
$ python3 manage.py db upgrade
$ python3 manage.py db --help
```