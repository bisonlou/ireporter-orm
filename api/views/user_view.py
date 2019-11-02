from flask import request, jsonify, render_template
import sys
import json
from api import app
from api.models.user import User
from api.database import db


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/users")
def users():
    data = User.query.all()
    users = [user.as_dict() for user in data]

    return jsonify({"data": users})


@app.route("/users/register", methods=["POST"])
def register():
    username = request.get_json()["username"]
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    phonenumber = request.get_json()["phonenumber"]

    new_user = User(
        username=username,
        email=email,
        password=password,
        phonenumber=phonenumber,
        isadmin=False,
    )

    error = False
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        if not error:
            data = User.query.all()
            users = [user.as_dict() for user in data]

            return jsonify({"data": users})
        else:
            return jsonify({"error": "failed!"})

@app.route("/users/delete", methods=["POST"])
def delete():
    userId = request.get_json()["userId"]

    error = False
    try:
        User.query.filter_by(id=userId).delete()
        db.session.commit()
    except:
        error = True
        print(sys.exc_info())
        db.session.rollback()
    finally:
        if not error:
            data = User.query.all()
            users = [user.as_dict() for user in data]

            return jsonify({"data": users})
        else:
            return jsonify({"error": "failed!"})

