#!/usr/bin/python3
"""All cities"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """all cities"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State, City.state_id == State.id)

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
