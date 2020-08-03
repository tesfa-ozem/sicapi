from flask import request, jsonify, send_from_directory, json, abort, url_for, g, Blueprint
from blue import db
from blue.models import User, Post, Photos
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from blue.utilities.utilities import Utilities
import datetime

mod = Blueprint('api', __name__)
token_auth = HTTPTokenAuth(scheme='Bearer')
basic_auth = HTTPBasicAuth()


@mod.route('/getCategories')
def get_categories():
    post = User(username='Tesfa', email='alphatesfa789@gmail.com',
                password_hash='1234')
    db.session.add(post)
    db.session.commit
    users = User.query.all()
    print(users[0])
    return 'ss'


@mod.route('/addPost')
def add_post():
    u = User.query.get(0)
    p = Post(body='my first post!', author=u)
    db.session.add(p)
    db.session.commit()
    posts = Post.query.all()
    print(posts)
    return 'post'


@mod.route('/photos', methods=['POST'])
def update_photo():
    project_id = request.form['projectId']
    if request.method == "POST":
        if request.files:
            time_stamp = str(datetime.datetime.now().strftime("%m-%d-%Y"))
            image = request.files["image"]
            with Utilities() as util:
                path = util.save_image(image, time_stamp)
                if not path:
                    return "wrong format"
                else:
                    new_path = "http://35.208.229.105/static/assets/images/{}".format(
                        path)
                    photo = Photos(photo=new_path, projects_id=project_id)
                    db.session.add(photo)
                    db.session.commit()
                    return "Success"

    return "ok"
