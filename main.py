from flask import Flask, render_template, url_for, jsonify, request
from hackernewsscraper import data_scraping
from passwordchecker import passwordcheck

app = Flask(__name__)


@app.route("/")
def index():
    houses = ["green", "yellow", "white", "brown"]
    top_news = data_scraping()
    return render_template("index.html", houses=houses, top_news=top_news)


@app.route("/passwordcheck/<password>", methods=['GET', 'POST'])
def testfn(password):
    # GET request
    if request.method == 'GET':
        message = passwordcheck(password)
        return jsonify(message)  # serialize and use JSON headers

    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

# @app.route("/<username>")
# def index(username):
#     return render_template("index.html", name=username)
