from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file
import json

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route('/soundboard', methods=['GET', 'POST'])
def soundboard():
	return render_template('soundboard.html')