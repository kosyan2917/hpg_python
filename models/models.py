from sqlalchemy import MetaData, Integer, String, Column, Table, ForeignKey
from sqlalchemy.orm import declarative_base

metadata = MetaData()


Base = declarative_base(metadata=metadata)


class BaseBoard(Base):
    __tablename__ = 'base_board'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    low = Column(Integer, nullable=True)
    high = Column(Integer, nullable=True)
    tags = Column(String(300), nullable=True)
    image = Column(String(300), nullable=False)
    points = Column(Integer, nullable=True)
    type = Column(String(100), nullable=False)
    games = Column(String(300), nullable=True)

