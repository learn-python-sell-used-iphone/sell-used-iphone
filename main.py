import logging
from flask import Flask, render_template
from model import db

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = "Sell used iphone"

        return render_template(
            "index.html", page_title=title,
        )

    return app 
