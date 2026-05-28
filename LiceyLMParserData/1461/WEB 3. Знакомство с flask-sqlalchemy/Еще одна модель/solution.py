from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=True)
    chief = Column(Integer, ForeignKey("users.id"))
    email = Column(String, nullable=True)
    members = Column(String, nullable=True)

    user = relationship("User")