import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'), nullable=False)
    job = Column(String, nullable=False)
    work_size = Column(Integer, nullable=False)
    collaborators = Column(String, nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, default=False)
    team_leader_rel = relationship("User", foreign_keys=[team_leader])