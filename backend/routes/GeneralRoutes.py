from flask_login import LoginManager
from model.Models import User
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

import routes.UserRoutes

