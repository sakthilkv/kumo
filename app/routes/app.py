from flask import Blueprint, jsonify, request, make_response, session, redirect, url_for,render_template
from ..table import Users, AnimeList
from ..auth import register,login
from .utils import jtools as jt
from ..config import status
main = Blueprint('main', __name__)
userdb = Users()
animedb = AnimeList()
@main.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            username = request.form['username']
            display_name = request.form['display-name']

            user = register(email, password)
            if user is not None:
                userdb.create_user(user.uid, username, email, display_name)
            else:
                print("Can't create User")
        except Exception as e:
            print(f"Error: {e}")
    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = userdb.get_email_by_username(username)

        if email is not None:
            try:
                session_token = login(email, password)
                session['user_token'] = session_token['localId']
                session['user_id'] = userdb.get_user_id(email)
                session.permanent = True
                return redirect('/home')
            except Exception as e:
                session.clear()
                return render_template('signin.html', error="Login failed. Please try again.")
        else:
            return render_template('signin.html', error="Username not found.")
    
    return render_template('signin.html')

@main.route('/home')
def home():
    if 'user_token' in session:
        return render_template('home.html')
    else:
        return redirect('/login')

@main.route('/add/<int:id>')
def add_anime(id):
    details = jt.preload_anime_details(id)
    try:
        animedb.create_entry(session['user_id'],id,details,status[1])
        return jsonify({"message": "Anime added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/shows')
def get_shows():
    if 'user_id' not in session:
        return jsonify({"error": "User not logged in"}), 403
    try:
        user_animes_list = animedb.get_user_animes(session['user_id'])
        return jsonify(user_animes_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@main.route('/logout')
def logout():
    session.clear()
    return redirect('/login')