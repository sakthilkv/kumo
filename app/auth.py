 
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('app/env/cred.json')
firebase_admin.initialize_app(cred)

def register(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )

        return user
    except firebase_admin.auth.AuthError as e:
        print(f'Error creating user: {e}')
        return None


def login(email, password):
    try:
        user = auth.get_user_by_email(email)
        print(f'Successfully retrieved user: {user.uid}')
        return user
    except firebase_admin.auth.UserNotFoundError:
        print('User not found')
        return None
    except firebase_admin.auth.AuthError as e:
        print(f'Error retrieving user: {e}')
        return None




