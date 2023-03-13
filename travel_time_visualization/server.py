from flask import Flask, jsonify,render_template,request
from config import API_KEY
import datetime
from collections import defaultdict
import requests
import pandas as pd
import sys
import logging
from itertools import repeat

app = Flask(__name__)
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

from multiprocessing.dummy import Pool as ThreadPool 
pool = ThreadPool(20) 
BASE_URL="https://maps.googleapis.com/maps/api/"
app.logger.debug(datetime.datetime.fromtimestamp(1498924020))

class GAPIError(Exception):
    status_code = 31337

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def makeRequest(url, API_KEY):
    url+="&key=%s"%API_KEY
    return requests.get(url).json()['rows'][0]['elements'][0]['duration_in_traffic']['value']
def getDistanceMatrix(origin,destination,mode,departure_time,traffic_model, API_KEY):
    #UTC Time
    url=BASE_URL+"distancematrix/json?"
    params="origins=%s&destinations=%s&mode=%s&departure_time=%s&traffic_model=%s"%(origin,destination,mode,departure_time,traffic_model)
    return makeRequest(url+params, API_KEY)

def getNearest(dt,offset):
    return dt + (datetime.datetime.min - dt) % datetime.timedelta(minutes=offset)

def getChartData(starting_address,destination_address, leave_after, hours_to_grab,API_KEY,OFFSET=15):
    start_date=getNearest(leave_after,15)
    request_times=defaultdict(dict)
    dts=[int(leave_after.timestamp())]
    
    for dt in (start_date + datetime.timedelta(minutes=offset) for offset in range(0,60*hours_to_grab,OFFSET)):
        dts.append(int(dt.timestamp()))
    
    request_times={}
    for traffic_model in ["best_guess","pessimistic","optimistic"]:
        results=pool.starmap(
            getDistanceMatrix, zip(repeat(starting_address),repeat(destination_address),repeat("car"),dts,repeat(traffic_model), repeat(API_KEY))
        )
        request_times[traffic_model]=results
        request_times["index"]=dts
    travel_times=pd.DataFrame.from_dict(request_times).set_index("index")/60
    viz_df=travel_times.reset_index()
    viz_df['x']=viz_df['index']*1000#Add milliseconds for JS datetime
    del viz_df['index']
    viz_json=viz_df.to_dict(orient="list")
    #to c3 Columns
    columns=[]
    for col,vals in viz_json.items():
        if col!="x":
            vals=[round(x) for x in vals]
        columns.append([col]+vals)
    return columns

@app.route("/")
def index():
    return render_template('index.html', API_KEY=API_KEY)
    
@app.route('/data')
def data():
    app.logger.debug(request.args)  
    leaveAfter=request.args.get("leaveAfter")
    leaveAfter=datetime.datetime.fromtimestamp(int(leaveAfter)/1000)
    USERS_API_KEY=request.args.get("API_KEY",default=API_KEY)
    now=datetime.datetime.now()
    if leaveAfter<now:
        leaveAfter=now
    try:
        response=getChartData(request.args.get("startingAddress"),request.args.get("destinationAddress"),leaveAfter,8, USERS_API_KEY)
        return jsonify(response)
    except:
        raise GAPIError("API Key no longer valid", status_code=31337)
    
    
@app.errorhandler(GAPIError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
