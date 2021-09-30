
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create a login manager object
login_manager = LoginManager()

app = Flask(__name__)
'''
POSTGRES = {
    'user': 'postgres',
    'pw': 'myPassword',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}'''

# Often people will also separate these into a separate config.py file
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost/postgres'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:/%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:/[hassan]'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbUserName:userNamePassword@localhost/dbName'
db = SQLAlchemy(app)
Migrate(app, db)

# We can now pass in our app to the login manager
login_manager.init_app(app)        # configure the application

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"