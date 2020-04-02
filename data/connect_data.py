from config import Base
from sqlalchemy import Column, String, Integer

class GroupLink(Base):
    # table
    __tablename__ = 'GroupLink'
    # struct
    id = Column(Integer(), primary_key=True)
    fr = Column(Integer())
    to = Column(Integer())