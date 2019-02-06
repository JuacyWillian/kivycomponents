import enum
from datetime import datetime
from functools import reduce

from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_uri = 'sqlite:///:memory:'
debug = False

db = create_engine(database_uri, echo=debug)
Base = declarative_base()
session = sessionmaker(bind=db)()

