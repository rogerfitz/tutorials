from flask import Flask, jsonify,render_template,request
import datetime
from collections import defaultdict
import requests
import pandas as pd
import sys
import logging
from itertools import repeat

app = Flask(__name__, template_folder=".")
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/mlb_asg_team_performance")
def mlb_asg_team_performance():
    return render_template('mlb_asg_team_performance.html')
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)