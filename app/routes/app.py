from flask import Blueprint, jsonify, request, make_response, session, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@main.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        session.permanent = True  
        session['username'] = request.form['username']
        return redirect(url_for('main.index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

