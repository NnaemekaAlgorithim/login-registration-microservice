#!/usr/bin/python3
"""Defines the User class."""
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base

class User(BaseModel, Base):
    """Represents a user for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table user.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store users.
        first_name (sqlalchemy String): The user's first name.
        last_name (sqlalchemy String): The user's last name.
        gender (sqlalchemy String): The user's gender.
        date_of_birth (sqlalchemy Date): The user's date of birth.
        phone_number (sqlalchemy String): The user's phone number.
        email (sqlalchemy String): The user's email address.
        address (sqlalchemy TEXT): The user's address.
        country_of_origin (sqlalchemy String): The user's country of origin.
        password (sqlalchemy String): The user's password.
    """
    __tablename__ = "user"
    first_name = Column(String(128))
    last_name = Column(String(128))
    gender = Column(String(128))
    date_of_birth = Column(Date)
    phone_number = Column(String(128))
    email = Column(String(128), nullable=False)
    address = Column(Text)
    country_of_origin = Column(String(128))
    password = Column(String(128), nullable=False)
    # Define a variable for backref (incase it is needed)
    # dynamic_backref = "user_reviews"
