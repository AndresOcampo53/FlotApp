from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://postgres:localhost@localhost:5432/Universidad')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()