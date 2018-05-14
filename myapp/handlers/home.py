
from myapp import app

from flask import render_template


@app.route('/')
def homepage():
    handlers = [
        ('city forecasts', '/search'),
        ('most popular', 'api/1/weather/getstats')
    ]
    return render_template('home.html', handlers=handlers)
