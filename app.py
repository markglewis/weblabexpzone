from flask import Flask, render_template, request, url_for, redirect, jsonify, send_file
import json

app = Flask(__name__)

@app.route('/soundboard', methods=['GET', 'POST'])
def index():
	return render_template("soundboard.html")
'''
@app.route('/return-file')
def return_file(filename):
    return send_file()
'''
