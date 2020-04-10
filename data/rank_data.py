from config import app, Base
from sqlalchemy import Column, String, Integer

class MessageCount(Base):
    
    __tablename__ = 'MessageCount'

    id = Column(Integer(), primary_key=True)
    person = Column(Integer())
    group = Column(Integer())
    count = Column(Integer())