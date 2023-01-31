from flask import Flask
from app.config import Config


from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
app.config["donwload_path"] = "E:/WorkDir/MyPortofolio/app/static/sendFiles"
# mail confgi
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "myportfolioApp2@gmail.com"
app.config["MAIL_PASSWORD"] = "mjsb sipy twzk zkdz"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)
