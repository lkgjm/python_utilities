""" Store Data in redis"""
import os

from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
bind_port = os.environ['BIND_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/', methods=["GET"])
def home_page():
    """ Get home page"""
    redis.incr('hits')
    total_hits = redis.get('hits').decode('utf-8')
    return render_template('index.html', redis_db=REDIS_HOST, redis_count=total_hits)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
