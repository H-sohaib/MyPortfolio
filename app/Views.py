# from app import demo_bp
from app import app, mail
from flask import render_template, send_from_directory, abort, request, Blueprint, redirect
from flask_mail import Message
import subprocess
from time import sleep
import os


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form["contactName"]
        email = request.form["contactEmail"]
        subject = request.form["contactSubject"]
        message = request.form["contactMessage"]
        # make the email
        msg = Message(
            subject,
            sender=app.config["MAIL_USERNAME"],
            recipients=['harraoui.sohaib1@gmail.com'])
        msg.body = f'from name: <{name}> that have email:< {email} > send u this msg :\n   {message} '
        try:
            mail.send(msg)
            return "OK"
        except Exception as e:
            print(f"ther is a execption : {e} ")
    return render_template("index.html", page="index")


@app.route('/download/<file>')
def download(file):
    try:
        return send_from_directory(app.config["DOWNLOAD_PATH"], file, as_attachment=True)
    except FileNotFoundError:
        abort(404)
    except Exception as e:
        print(e)
        return "Internal Error 500 !"


@app.route("/works")
def works():
    return render_template("work.html")


demo_bp = Blueprint('demo_bp', __name__)


@demo_bp.route('/TaskAPP')
def taskapp():

    if os.getcwd() == "E:\WorkDir\MyPortfolio":
        print("directory chenged")
        os.chdir("app/static/Projects/TaskAPPjQuery")

    print(os.getcwd())
    out = subprocess.run([".venv\\Scripts\\activate.bat"],
                         stdout=subprocess.PIPE,
                         text=True,
                         )
    # print("activate !!")
    # print(out)
    out = subprocess.run(["python", "query.py"],
                         stdout=subprocess.PIPE,
                         text=True,
                         )
    # print("create Tables !!")
    # print(out)
    # out = subprocess.run(["flask", "run", "-h", "localhost", "-p", "3000"],
    #                      stdout=subprocess.PIPE,
    #                      text=True,
    #                      )
    out = subprocess.Popen(["flask", "run", "-h", "0.0.0.0", "-p", "3000"],
                           stdout=subprocess.PIPE,
                           text=True
                           )
    print("python out : ")
    print(out)
    sleep(1)

    return redirect("http://192.168.233.219:3000/")


app.register_blueprint(demo_bp, url_prefix='/demo')
