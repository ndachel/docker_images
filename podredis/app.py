import socket
from flask import Flask, render_template, request
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379)

@app.route('/')
def home():
    count = redis.incr('hits')
    hostname =  hostname = socket.gethostname()
    retStr = render_template('index.html',deployment_color = 'RED', line_back = '#FF0000',count = count, hostname = hostname)
    return(retStr)

@app.route('/health')
def health():
    retStr = render_template('health.html', deployment_color = "RED")
    return(retStr)

#@app.route('/redis')
#def redis():
#    return("Redis query:")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

