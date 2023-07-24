from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from database import db

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

class User(db.Model): #parent to UserInteractionWithVA
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    # _password_hash = db.Column(db.String)
    userinteractions = db.relationship('UserInteractionWithVirtualAssistant', backref='interactions') #if we have a User instance, we can access their interactions using 'user.interactions'

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def __repr__(self):
        return f'<User {self.username}>'

class UserInteractionWithVirtualAssistant(db.Model): #child to User Table
    __tablename__ = "userinteractions"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    parent_id = db.Column(db,Integer, db.ForeignKey('userinteractions.id'), nullable=True) 
    user_input_speech = db.Column(db.String)
    date_of_speech = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'user_input_speech': self.user_input_speech,
            'date_of_speech': self.date_of_speech
        }

    def __repr__(self):
        return f'<UserInteractionWithVirtualAssistant {self.user_input_speech}>'


class ApiResponse(db.Model): 
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    interaction_id = db.Column(db.Integer, db.ForeignKey('userinteractions.id'))
    
     response_text = db.Column(db.String)
     response_date = db.Column(db.DateTime, default=datetime.utcnow)

     def to_dict(self):
        return {
            'response_text': self.response_text,
            'response_date': self.response_date
        }

        def __repr__(self):
            return f'<ApiResponse  {self.response_text}>'

