from flask import Blueprint, jsonify, request, make_response, session, redirect, url_for,render_template
from ..table import Users
from ..auth import register
main = Blueprint('main', __name__)
userdb = Users()
@main.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            user = register(request['email'],request['password'])
        except:
            user = None
        if user is not None:
            userdb.create_user(user.uid,request['username'],request['email'],request['display-name'])
        else:
            print("Can't create User")
    return render_template('signup.html')