from datetime import datetime
from utils.GenericResponses import GenericResponses
from utils.ValidationRules import ValidationRules
from model.Models import User, UserType
from flask_login import login_user, login_required, current_user
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from routes.GeneralRoutes import db, app
import logging

valRules = ValidationRules()
logger = logging.getLogger(__name__)

@app.route('/test', methods=['GET'])
def test():
    user = User()
    return 'it works!' + user.query.all()[0].name

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    return 'it works!' + current_user.username

@app.route('/login', methods=['POST'])
def login_post():
    if "password" not in request.json:
        return GenericResponses.specific_error_msg("Password is required for login!")
    
    password = request.json["password"]

    if "username" in request.json:
        username = request.json["username"]
        user = User.query.filter_by(username=username).first()
    else:
        email = request.json["email"]
        user = User.query.filter_by(email=email).first()        

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        logger.error("Wrong user/password!")
        return GenericResponses.specific_error_msg("Wrong user/password")
    else:
        login_user(user, remember=True)

    # if the above check passes, then we know the user has the right credentials
    return GenericResponses.success()

@app.route('/register', methods=['POST'])
def register_post():
    try:
        result = valRules.validate_user(request.json)
        if len(result["errors"]) > 0:

            return GenericResponses.specific_error("Error trying to register user", result["errors"])

        email = request.json["email"]
        username = request.json["username"]
        password = request.json["password"]
        dateOfBirth = request.json["dateOfBirth"]

        user = User(
                email=email,
                password=generate_password_hash(password),
                userTypeId=UserType.REGULAR,
                username=username,
                dateOfBirth=datetime.strptime(dateOfBirth, "%m/%d/%Y")
        )
        
        db.session.add(user)
        db.session.commit()

        userTest = User.query.filter_by(email=email).first()
    except Exception as err:
        #some error happened
        logger.error("Error trying to register user!")

        return GenericResponses.error(err)

    return GenericResponses.success()

@app.route('/confirm', methods=['GET'])
def confirm_email():
    
    #confirm user email

    return GenericResponses.success()