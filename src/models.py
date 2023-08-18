import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Define columns for the table follower
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user_to_id = Column(Integer, ForeignKey('user.ID'))

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(50))
    url = Column(String(100))
    post_id = Column(Integer, ForeignKey('post.ID'))

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(50))
    author_id = Column(Integer, ForeignKey('user.ID'))
    post_id = Column(Integer, ForeignKey('post.ID'))

class Post(Base):
    __tablename__ = 'post'  # Corrected table name
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    media = relationship(Media, backref='post', lazy=True)
    comment = relationship(Comment, backref='post', lazy=True)

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    email = Column(String(50))
    followers = relationship(Follower, backref='user', lazy=True)
    posts = relationship(Post, backref='user', lazy=True)
    comments = relationship(Comment, backref='user', lazy=True)

    def to_dict(self):
        return {}

# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
