from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
 

  #creation of app
app = Flask(__name__ )
app.config['SECRET_KEY'] = '89d9a808fe229b4cf4e66a3b51e52fdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from pitch import routes 