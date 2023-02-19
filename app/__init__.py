from flask import Flask, Blueprint
from flask_mail import Mail
app = Flask(__name__)
app.config.from_object("config.Config")
# if (app.config["ENV"] == "pro"):
#     app.config.from_object("config.Pro_config")
# elif app.config["ENV"] == "dev":
#     app.config.from_object("config.Dev_config")

# Demo part

mail = Mail(app)
