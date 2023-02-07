from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bycrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLACHEMY_DATABASE_URI'] = "mysql://username:password@localhost/users'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'

from UniHatch import routes
