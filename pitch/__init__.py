from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 

  #creation of app
app = Flask(__name__ )
app.config['SECRET_KEY'] = '89d9a808fe229b4cf4e66a3b51e52fdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from pitch import routes 