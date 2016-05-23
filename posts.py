from mongoengine import *

class Post(Document):
    title = StringField()
    link = StringField()
    img = StringField()