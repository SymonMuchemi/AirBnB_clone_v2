#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")

    @property
    def cities(self):
        """returns the list of city instance with state_id same as current state.id"""
        from models import storage
        from city import City
        cities = []
        all_cities = storage.all(City)

        # check if city has similar state_id
        for city in all_cities:
            if city.state_id == self.id:
                cities.append(city)
        return cities
