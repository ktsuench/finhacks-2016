import os
from flask import Flask, render_template
import requests
import re
import string

app = Flask(__name__)
@app.route('/')
def hello():
	episodes_list = [{'num': '1', 'src': "ep1"}, {'num': '2', 'src': "ep2"}, {'num': '3', 'src': "ep3"}, {'num': '4', 'src': "ep4"}, {'num': '5', 'src': "ep5"}]
	return render_template('test.html', episodes=episodes_list)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
