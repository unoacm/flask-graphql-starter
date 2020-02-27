from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    country = Column(String)
    region = Column(String)
    city = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location, backref=backref(
        'users', uselist=True, cascade='delete, all'))

    def __init__(self, username, password, location):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.location = location
