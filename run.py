from app import app, Views
from flask_minify import Minify


Minify(app=app, html=True, js=True, cssless=True)

if __name__ == "__main__":
    app.run(debug=True)
