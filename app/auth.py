import firebase_admin
from firebase_admin import credentials, auth
from config import firebase_admin_config,firebase_client_config
import json,requests
cred = credentials.Certificate(firebase_admin_config)
firebase_admin.initialize_app(cred)

def check_if_user_exists(email):
    try:
        user = auth.get_user_by_email(email)
        return True
    except auth.UserNotFoundError:
        return False
    except Exception as e:
        return None

def register(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )

        return user
    except firebase_admin.auth.AuthError as e:
        return None


def login(email, password):
    try:
        user = auth.get_user_by_email(email)
        return user
    except firebase_admin.auth.UserNotFoundError:
        print('User not found')
        return None
    except firebase_admin.auth.AuthError as e:
        print(f'Error retrieving user: {e}')
        return None

def send_password_reset_email(email):
    if check_if_user_exists(email):

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={firebase_client_config['apiKey']}"
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({
            "requestType": "PASSWORD_RESET",
            "email": email
        })
        
        response = requests.post(url, headers=headers, data=payload)
        
        if response.status_code == 200:
            return True
        else:
            return False
    else:
        return False

def send_email_verification(email):
    link = generate_email_verification_link(email)
    if not link:
        return False
    
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({
        "requestType": "VERIFY_EMAIL",
        "email": email
    })
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        return True
    else:
        return False

def is_email_verified(email):
    try:
        user = auth.get_user_by_email(email)
        return user.email_verified
    except auth.UserNotFoundError:
        return False
    except Exception as e:
        return False

print(login("sakthilk13072005@gmail.com","87654321"))