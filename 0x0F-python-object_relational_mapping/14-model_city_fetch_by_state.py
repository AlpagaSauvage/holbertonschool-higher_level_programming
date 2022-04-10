#!/usr/bin/python3
""" Cities in state
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from model_city import Base, City


if __name__ == "__main__":

    ml = 'mysql+mysqldb://'
    lh = '@localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('{}{}:{}{}/{}'.format(ml, user, passwd, lh, db))
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    cityr = session.query(City).all()
    stater = session.query(State).all()

    for city in cityr:
        for state in stater:
            if (state.id == city.state_id):
                print("{}: ({}) {}".format(state.name, city.id, city.name))
