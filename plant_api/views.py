import requests
from flask import render_template
from plant_api import app


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
