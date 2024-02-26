#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition of the State class.

    This class represents a state in the 'states' table of a MySQL database,
    with an auto-generated, unique 'id' as a primary key and a 'name' attribute
    that stores the name of the state, which cannot
    be null and is limited to 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                        sys.argv[2],
                                                        sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
