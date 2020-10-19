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

@app.route('/blog', methods=['GET', 'POST'])
def blog():
	return render_template('blog.html')

@app.route('/todo', methods=['GET', 'POST'])
def todo():
	return render_template('todo.html')

@app.route('/soundboard', methods=['GET', 'POST'])
def soundboard():
	return render_template('soundboard.html')

@app.route('/lipsmack', methods=['GET', 'POST'])
def lipsmack():
	return render_template('lipsmack.html')

@app.route('/musictest', methods=['GET', 'POST'])
def musictest():
	return render_template('musictest.html')

@app.route('/myage', methods=['GET', 'POST'])
def myage():
	return render_template('myage.html')