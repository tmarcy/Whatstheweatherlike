
from google.appengine.ext import ndb


class City(ndb.Model):
    """ Model to store cities data
        """
    name = ndb.StringProperty()
    counter = ndb.IntegerProperty(default=0)
