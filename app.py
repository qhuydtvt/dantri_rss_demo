from flask import Flask, render_template
from mongoengine import connect
from posts import Post

app = Flask(__name__)


host = "ds011893.mlab.com"
port = 11893
db_name = "c4e_rss"
user_name = "c4e"
password = "codethechange"

connect(db_name, host=host, port=port, username=user_name, password=password)

@app.route('/')
def hello_world():
    posts = Post.objects
    print("Loading ok")
    return render_template("index.html", posts = posts)

if __name__ == '__main__':
    app.run()
