import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

jobs_collaborators = Table(
    'jobs_collaborators', SqlAlchemyBase.metadata,
    Column('job_id', Integer, ForeignKey('jobs.id')),
    Column('user_id', Integer, ForeignKey('users.id')))


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey('users.id'))
    job = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True)
    start_date = Column(DateTime, default=datetime.datetime.now)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, default=False)

    collaborators = relationship('User', secondary='jobs_collaborators', backref='jobs')