#!/usr/bin/python3
""" new database """
from sqlalchemy import (create_engine)from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
from models.user import User
from models.base_model import Base
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review



class DBStorage:
    """ creates db"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for i in query:
                key = "{}.{}".format(type(i).__name__, i.id)
                dic[key] = i
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for i in lista:
                query = self.__session.query(i)
                for j in query:
                    key = "{}.{}".format(type(j).__name__, j.id)
                    dic[key] = j
        return (dic)

    def new(self, obj):
        """
        adds a new element to the table
        """
        self.__session.add(obj)

    def save(self):
        """
        save changes to the table
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an element from the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        configures the db
        """
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s)
        self.__session = Session()

    def close(self):
        """ 
        calls the remove method
        """
        self.__session.close()