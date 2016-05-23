from flask import Flask, render_template
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient("mongodb://c4e:codethechange@ds011893.mlab.com:11893/c4e_rss")
db = client.get_default_database()


@app.route('/')
def hello_world():
    posts = db["posts"].find()
    print("Loading ok")
    return render_template("index.html", posts = posts)

if __name__ == '__main__':
    app.run()
