from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
engine = create_engine('sqlite:///kumo.db', echo=True)
Base = declarative_base()

class User_DB(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    uid = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    profile_picture = Column(String)
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
    name = Column(String, nullable=False)
    poster = Column(String, nullable=False)
    status = Column(String, nullable=False)
    episodes = Column(Integer, nullable=True)
    review = Column(String, nullable=True)

Base.metadata.create_all(engine) 
