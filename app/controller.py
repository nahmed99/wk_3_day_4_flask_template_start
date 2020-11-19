from flask import render_template
from app import app

@app.route('/') # listen to the home/root
def index():
    return render_template('index.html', title="Home")