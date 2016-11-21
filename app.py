import os
from flask import Flask, render_template
from flask import request
import requests
import re
import string
import urllib
import urllib.request
import urllib.error
import json
import calendar

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', result=None)

@app.route('/result', methods=["POST"])
def apicall():
    id = request.form["id"]
    chk = []
    data = {
        "Inputs": {
            "input1": {
                "ColumnNames": ["month", "price", "item"],
                "Values": []
            },
        },
        "GlobalParameters": {}
    }
    for i in range(1,13):
        data["Inputs"]["input1"]["Values"].append([ str(i), "0", id ])

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/24af1e57b2794253957d65b08d00a725/services/dca5e0834086488e986f1efd0375ae2f/execute?api-version=2.0&details=true'
    api_key = 'IQW3L6TA21jChGgRgm8Z2w8xGeYtpUISi3b7fXY+/DKw1O7Mxrklwd3PKxUTHBuu43HybpCOtLfN+AuPOkYmbw==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read().decode("utf-8")
        chk.append(json.JSONDecoder().decode(result))
    except(urllib.error.HTTPError):
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))

    ref = chk[0]["Results"]["output1"]["value"]["Values"]
    minN = ref[0][3]
    res = ref[0][0]
    for i in range(1,len(ref)):
        if(ref[i][3] < minN):
            res = ref[i][0]
    
    return render_template('index.html', result=calendar.month_name[int(res)])

@app.route('/test')
def test():
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
