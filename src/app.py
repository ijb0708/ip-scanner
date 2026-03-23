from flask import Flask, render_template, jsonify
from scanner import get_network_status
import json
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

@app.route('/')
def index():

    network_data = get_network_status("10.1.1.0/24")

    return render_template('index.html', network=network_data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)