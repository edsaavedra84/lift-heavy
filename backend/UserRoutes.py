from app import app
from model.Models import User

@app.route('/test', methods=['GET'])
def test():
    user = User()
    return 'it works!' + user.query.all()[0].name