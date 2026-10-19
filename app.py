from flask import Flask, render_template
import os, json
from flask_sock import Sock 

app = Flask(__name__)
sock = Sock(app)


"""
/ route 
"""
@app.route('/')
def home():
    return  render_template('home.html')

"""
/ws route using  Sock 
"""
@sock.route('/ws')
def websocket(ws):
    while True:
        data = ws.receive()
        if data is None:
            break
        ws.send(f"Received: {data}")


app.run(debug=True, host='0.0.0.0', port=8000)