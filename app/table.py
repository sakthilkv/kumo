from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
import uuid
from .config import accnt_status
from .models import User_DB,engine
Session = sessionmaker(bind=engine)

class Users:
    def get_email_by_username(self,username):
        session = Session()
        try:
            user = session.query(User_DB).filter_by(username=username).first()
            if user:
                return user.email
            else:
                return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        finally:
            session.close()
    def get_user_id(self,email):
        session = Session()
        try:
            user = session.query(User_DB).filter_by(email=email).first()
            if user:
                return user.user_id
            else:
                return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
        finally:
            session.close()
    def create_user_id(self):
        userid = uuid.uuid4()
        return userid.hex

    def create_user(self, uid, username, email, display_name):
        session = Session()
        try:
            new_user = User_DB(
                user_id=self.create_user_id(),
                uid=uid,
                username=username,
                email=email,
                display_name=display_name,
                account_status=accnt_status[0]
            )
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Failed to create user: {e}")
            return None
        finally:
            session.close()

    def get_user_data(self):
        pass