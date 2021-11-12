from flask import Flask
from markupsafe import escape
from json import dumps as json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Yosafat", 22)

app = Flask(__name__)


@app.route('/person')
def getPerson():
    return json(person.__dict__)


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


if __name__ == '__main__':
    app.run(debug=True)
