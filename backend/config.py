# building the api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# want the frontend to communicate the backend
app = Flask(__name__)
# wrap app in CORS
# disable error
CORS(app)

# stroing the sqlite database and need to specify the file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# track all the changes which we made in the database.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# instace of the db
db = SQLAlchemy(app)