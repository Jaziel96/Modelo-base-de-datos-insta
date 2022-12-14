import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

   


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__="comment"
    id=Column(Integer, primary_key=True)
    comment_text=Column(String(500),nullable=False)
    author_id=Column(Integer, ForeignKey('user.id'))
    author=relationship(User)
    post_id=Column(Integer, ForeignKey('post.id'))
    post=relationship(Post)

class Media(Base):
    __tablename__="Media"
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = "follower"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id=Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from=relationship(User)
    user_to_id=Column(Integer, ForeignKey('user.id'))
    user_to=relationship(User)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')