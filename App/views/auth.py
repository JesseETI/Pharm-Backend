from flask import Blueprint, redirect, render_template, request, abort, jsonify
from flask_jwt import jwt_required, current_identity
import json

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

from App.controllers import (
    create_user,
    get_user,
)

# Test to get user email
@auth_views.route('/user')
@jwt_required()
def get_user_details():
    user = get_user(current_identity.email)
    return jsonify(user.toDict())


#Sign up endpoint
@auth_views.route('/signup', methods=["POST"])
def signup():
    #get user's data from form
    first_name = request.json.get('fname')
    last_name = request.json.get('lname')
    email = request.json.get('email')
    password = request.json.get('password')
    allergies = request.json.get('allergies')
    medicines = request.json.get('medications')
    
    if email is None or password is None: #missing arguments
        abort(400) 

    user = get_user(email) # if this returns a user, then the email already exists in database

    if user: # if a user is found, abort
        abort(400)
    
    #create user and jsonify their information for storage
    newUser = create_user(first_name, last_name, email, password, allergies, medicines, role = 1)
    return jsonify(newUser.toDict())