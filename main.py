from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route('/')

    def index():
        title = "Sell used iphone"
        return render_template("index.html", page_title= title, weather= weather, news_list= news)
    return app 