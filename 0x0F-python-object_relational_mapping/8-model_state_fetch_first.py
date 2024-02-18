#!/usr/bin/python3
"""import modules"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).first()

    if (states):
        print("{}: {}".format(State.id, State.name))
    else:
        print("Nothing")
