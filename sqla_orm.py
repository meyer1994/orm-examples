from datetime import datetime

from sqlalchemy import Column, ForeignKey, Text, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    home_id = Column(Integer, ForeignKey('team.id'))
    away_id = Column(Integer, ForeignKey('team.id'))
    home = relationship(Team, foreign_keys=[home_id])
    away = relationship(Team, foreign_keys=[away_id])


engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


from data import matches

session = Session()

for match in matches:
    home = Team(name=match['home'])
    away = Team(name=match['away'])
    match = Match(date=match['date'], home=home, away=away)

    # Save
    session.add(home)
    session.add(away)
    session.add(match)
    session.commit()


