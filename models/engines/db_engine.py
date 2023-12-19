#!/usr/bin/python3
"""Defines the DBStorage engine."""
from flask_bcrypt import check_password_hash
from os import getenv
from models.user_model import User
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from pymysql import connect, cursors


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+pymysql://{}:{}@{}/{}".
                                      format(getenv("MYSQL_USER"),
                                             getenv("MYSQL_PWD"),
                                             getenv("MYSQL_HOST"),
                                             getenv("MYSQL_DB")),
                                     )

    def all(self, cls=None):
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)
    
    def get_user(self, email=None, password=None):
        """Retrieve a user from the database by email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            User: The matching User object if found, None otherwise.
        """
        user = self.__session.query(User).filter(User.email == email).first()

        if user and check_password_hash(user.password, password):
            return user

        return None

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
