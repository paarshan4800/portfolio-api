from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail

import logging
import os
import dotenv

logging.basicConfig(filename="mailer.log", level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s")

app = Flask(__name__)
api = Api(app)
CORS(app)

dotenv.load_dotenv()

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MY_EMAIL'] = os.getenv('MY_EMAIL')

mail = Mail(app)

from api import routes
