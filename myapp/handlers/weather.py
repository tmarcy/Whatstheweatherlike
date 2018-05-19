
from flask import render_template, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import required, Email, length
from myapp import app
from myapp.models.City import City
import logging
import json
import urllib, urllib2


class LoginForm(FlaskForm):
    email = StringField('email', [required(), Email()])
    password = PasswordField('password', [required(), length(min=8, max=35)])
    submit = SubmitField('submit', [required()])


class MyForm(FlaskForm):
    city = StringField('city', [required()])
    submit = SubmitField('search', [required()])


@app.route('/login', methods=['GET'])
def show_loginForm():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/login', methods=['POST'])
def submit_loginForm():
    form = LoginForm(request.form)
    if not form.validate():
        return render_template('login.html', form=form), 400

    session['user'] = form.email.data
    return redirect('/')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    del session['user']
    return redirect('/')


@app.route('/search', methods=['GET'])
def showForm():
    form = MyForm()
    return render_template('search.html', form=form)


@app.route('/search', methods=['POST'])
def submitForm():
    form = MyForm(request.form)
    if not form.validate():
        return render_template('search.html', form=form), 400

    city_inserted = form.city.data

    # save data in the Datastore
    qry = City.query(City.name == city_inserted).get()
    if not qry:
        new_c = City(name=city_inserted, counter=1)
        new_c.put()
        logging.info('Correctly inserted {}'.format(city_inserted))
    else:
        qry.counter = qry.counter+1
        qry.put()
        logging.info('Correctly update {}'.format(city_inserted))

    # use Metaweather API
    url = 'https://www.metaweather.com/api/location/search/'
    params = urllib.urlencode({'query': city_inserted})
    myurl = '{}?{}'.format(url, params)
    logging.info('myurl: {}'.format(myurl))

    req = urllib2.Request(myurl)
    urlopen = urllib2.urlopen(req)
    content = urlopen.read()
    risp = json.loads(content)
    woeid = str(risp[0]['woeid'])

    url2 = 'https://www.metaweather.com/api/location/'
    myurl2 = '{}{}/'.format(url2, woeid)
    logging.info('myurl: {}'.format(myurl2))
    req2 = urllib2.Request(myurl2)
    urlopen2 = urllib2.urlopen(req2)
    content2 = urlopen2.read()
    resp = json.loads(content2)

    tmin = []
    tmax = []

    for each in resp['consolidated_weather'][1:]:
        tmin.append(each['min_temp'])
        tmax.append(each['max_temp'])

    mmin = min(tmin)
    mmax = max(tmax)

    return render_template('response.html', resp=resp, tmin=tmin, tmax=tmax, mmin=mmin, mmax=mmax)
