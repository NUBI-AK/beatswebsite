from flask import Flask
from datetime import datetime
from models import db, Beat

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', 'False')
app.config['SITE_URL'] = os.environ.get('SITE_URL')

db.init_app(app)

# Get the absolute path of the project directory
  # Load environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Use environment variable if present, otherwise fall back to the explicit sqlite path
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'createbeats.db')

import routes
routes.init_app(app)


@app.context_processor
def inject_current_year():
  return {"current_year": datetime.now().year}


if __name__ == "__main__":
  with app.app_context():
    db.create_all()

  app.run(debug=True)

