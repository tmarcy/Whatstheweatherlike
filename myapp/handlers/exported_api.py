
from myapp import app
from flask import make_response
from myapp.models.City import City
import json


@app.route('/api/1/weather/getstats', methods = ['GET'])
def showpop():

    qry = City.query().order(-City.counter).fetch(3)

    my_data = []

    for each in qry:
        mydic = {}
        mydic['name'] = each.name
        mydic['counter'] = each.counter
        my_data.append(mydic)

    json_response = {}
    json_response['data'] = my_data
    json_response['status'] = 'OK'
    json_response['message'] = 'Successfully returned the resource.'
    response = make_response(json.dumps(json_response, ensure_ascii=True), 200)
    response.headers['content-type'] = 'application/json'
    return response
