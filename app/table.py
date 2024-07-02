from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from config import Base, engine, accnt_status
from sqlalchemy.orm import sessionmaker
import uuid

class User_DB(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    uid = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    profile_picture = Column(String, default='default.jpg')
    display_name = Column(String, nullable=False)
    bio = Column(String, default="One small episode for a weeb, one giant leap for anime.")
    location = Column(String, default='Wano')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    account_status = Column(Integer, nullable=False)

class Anime_DB(Base):
    __tablename__ = 'users_anime'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    anime_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    episode_no = Column(Integer)
    review = Column(String)

Session = sessionmaker(bind=engine)
session = Session()

class Users:
    def create_user_id():
        userid = uuid.uuid4()
        return userid.hex

    def create_user(uid,username,email,display_name):
        new_user = User_DB(
            user_id= create_user_id(),
            uid=uid,
            username=username,
            email=email,
            display_name=display_name,
            account_status=accnt_status[0]
        )
        session.add(new_user_anime)
        session.commit()

