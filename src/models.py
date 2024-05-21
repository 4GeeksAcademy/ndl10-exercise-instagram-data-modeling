import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    Id = Column(Integer, nullable = False, primary_key= True)
    FirstName = Column(String(19), nullable = False)
    LastName = Column(String(19), nullable = False)
    Email = Column(String(60), nullable = False)

    def serialize(self):
        return {
            'Id': self.Id,
            'FirstName': self.FirstName,
            'LastName': self.LastName,
            'Email': self.Email
        }
        

class Follower(Base):
    __tablename__ = 'follower'

    Id = Column(Integer, nullable= False, primary_key = True)
    Name = Column(String(20), nullable = False)
    Email = Column(String(60), nullable = False)

    def serialize(self):
        return   {
            'Id': self.Id,
            'Name': self.Name,
            'Email': self.Email
        }

      

class Post(Base):
    __tablename__ = 'post'

    Id = Column(Integer, nullable= False, primary_key= True)
    User_id = Column(String,  ForeignKey(User.Id), nullable= False,)

    def serialize(self):
        return{
               'Id': self.Id,
               'User_id': self.User_id
            }
            
class Type(enum.Enum):
    photo = 'photo'
    video = 'video'


class Media(Base):
    __tablename__ = 'media'

    Id = Column(Integer, nullable = False, primary_key = True)
    Type = Column(Enum(Type), nullable = False)
    Url = Column(String, nullable= False)
    Post_id = Column(Integer, ForeignKey(Post.Id), nullable= False,)

    def serialize(self):
        return {
            'Id': self.Id,
            'Type': self.Type,
            'Url' : self.Url,
            'Post_id': self.Post_id

        }
    
class Comment(Base):
    __tablename__ = 'Comment'

    Id = Column(Integer, nullable= False, primary_key= True)
    Comment_text = Column(String, nullable = False)
    Author_id = Column(String,ForeignKey(User.Id), nullable = False)
    Post_id = Column(Integer, ForeignKey(Post.Id), nullable= False,)

    def serialize(self):
        return {
            Id : self.Id,
            Comment_text: self.Comment_text,
            Author_id: self.Author_id,
            Post_id: self.Post_id
        }


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
