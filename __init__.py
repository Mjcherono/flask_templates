from flask import Flask
from .config import DevConfig

#Create an app instance
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

#Import views file from the app folders to assist in view creation
from app import views
