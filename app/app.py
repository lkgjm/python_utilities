""" Store Data in redis"""
import os

from flask import Flask, render_template, request, url_for, flash, redirect

from redis import Redis

app = Flask(__name__)
app.config['SECRET_KEY'] = '9f23e25f0b131d6df4004485c84d8db3936e0666bf4fdbde'

bind_port = os.environ['BIND_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)
redis.incr('hits')
total_hits = redis.get('hits').decode('utf-8')
messages = [{'title': REDIS_HOST + ' on port ' + REDIS_PORT,
             'content': total_hits}]


@app.route('/', methods=["GET"])
def index():
    """ Get home page"""
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
