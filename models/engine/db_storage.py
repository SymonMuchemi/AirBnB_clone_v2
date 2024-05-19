#!/usr/bin/python3
"""engine that handles database queries"""
import os

from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """manages storage of hbnb models in mysql database"""
    __engine = None
    __session = None

    classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def __init__(self):
        """initializing an instance of DBStorage"""
        hbnb_mysql_user = os.getenv('HBNB_MYSQL_USER')
        hbnb_mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
        hbnb_mysql_host = os.getenv('HBNB_MYSQL_HOST')
        hbnb_mysql_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_env')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                hbnb_mysql_user,
                hbnb_mysql_pwd,
                hbnb_mysql_host,
                hbnb_mysql_db
            ),
            pool_pre_ping=True
        )

        # drop all tables if the environment variable HBNB_ENV is equal to test
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary of all object of a class cls
        if cls in None, a dictionary of all objects of all classes is returned
        """
        obj_dict = {}
        if cls is not None and cls in DBStorage:
            cls_objs = self.__session.query(cls).all()
            for obj in cls_objs:
                obj_dict[cls + "." + obj.id] = obj
        instance_objs = {}
        for cls_obj in DBStorage.classes:
            list_of_obj = self.__session().query(cls_obj)
            for obj in list_of_obj:
                instance_objs[cls + "." + obj.id] = obj
        return instance_objs
