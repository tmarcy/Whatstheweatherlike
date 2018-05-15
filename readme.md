# Project Title

What's the Weather Like?

## The project in short

Simple Google App Engine Web Application example, written in Python 2.7, using MetaWheater site API 
(see references in "Built With" section).
The user is able to see his favourite city weather forecasts for the next five days.

## Specifications

* There is user login/logout mechanism.
* A form is used to retrieve users' searches data (city name).
* The app response shows: date, maximum temperature, minimum temperature (with blue color, when the day is the coldest, 
red color, when the day is the hottest, black color otherwise).
* The city name and a counter are saved automatically in the Datastore.
* An API GET is given; it shows the 3 most popular cities requested by users, in JSON format.

## Before starting
Add a lib folder to the project, in which you have to install the libraries listed in "requirements.txt" file.

## Built With

* [Google App Engine](https://cloud.google.com/appengine/doc) - Platform used
* [Flask](http://flask.pocoo.org/) - The microframework for Python used
* [Metaweather API](https://www.metaweather.com/) - API used

## Author

* **Marcella Tincani** - [Marcella](https://github.com/tmarcy)
