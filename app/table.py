from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
import uuid
from .config import accnt_status,status
from .models import User_DB,Anime_DB,Users_Anime_DB,engine
#from routes.utils import jtools as jt
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

class UserAnime:

    def create_entry(self,user_id,anime_id,anime,status,episode=None,review=None):
        session = Session()
        try:
            new_entry = Users_Anime_DB(
                user_id = user_id,
                anime_id = anime_id,
                name = anime[0],
                poster = anime[1],
                status = status,
                episodes = episode,
                review = review
            )
            session.add(new_entry)
            session.commit()
        except Exception as e:
            session.rollback()
            return None
        finally:
            session.close()

    def get_user_animes(self,user_id):
        session = Session()
        try:
            user_animes = session.query(Users_Anime_DB).filter_by(user_id=user_id).all()

            if not user_animes:
                return None

            user_animes_list = []
            for anime in user_animes:
                user_animes_list.append({
                    "id": anime.id,
                    "user_id": anime.user_id,
                    "anime_id": anime.anime_id,
                    "name": anime.name,
                    "poster": anime.poster,
                    "status": anime.status,
                    "episodes": anime.episodes,
                    "review": anime.review
                })

            return user_animes_list

        except Exception as e:
            return None
        
        finally:
            session.close()

class Anime:

    def add_anime_metadata(self,anime_metadata):
        session = Session()
        genres_str = ', '.join(anime_metadata.genres) if anime_metadata.genres else None
        anime = Anime_DB(
            id=anime_metadata.anime_id,
            title_jp=anime_metadata.title_jp,
            title_en=anime_metadata.title_en,
            poster=anime_metadata.poster,
            large_poster=anime_metadata.large_poster,
            title_type=anime_metadata.title_type,
            airing=anime_metadata.airing,
            score=anime_metadata.score,
            year=anime_metadata.year,
            genres=genres_str
        )
        session.add(anime)
        session.commit()

    def check_animeid(self,id):
        session = Session()
        return session.query(Anime_DB).filter_by(id=id).first()

    