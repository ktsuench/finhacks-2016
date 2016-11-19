import os
from flask import Flask, render_template
import requests
import re
import string

app = Flask(__name__)
@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/test')
def test():
	return render_template('test.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
