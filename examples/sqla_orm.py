from datetime import datetime

from sqlalchemy import Column, ForeignKey, Text, DateTime, Integer, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

    players = relationship('Player')

    # Copied from:
    #   https://stackoverflow.com/a/37157484/5092038
    matches = relationship(
        'Match',
        primaryjoin='or_(Team.id == Match.home_id, Team.id == Match.away_id)')


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)

    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team = relationship('Team')


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False)

    home_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    away_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    home = relationship('Team', foreign_keys=[home_id], backref='home')
    away = relationship('Team', foreign_keys=[away_id], backref='away')

    home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)

    league_id = Column(Integer, ForeignKey('league.id'), nullable=False)
    league = relationship('League', foreign_keys=[league_id])


class League(Base):
    __tablename__ = 'league'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    matches = relationship('Match')



engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


import data

# Insert teams
teams = [Team(name=t) for t in data.TEAMS]
session.add_all(teams)
session.commit()

# Get teams
for team in session.query(Team).all():
    print(team.id, team.name)


# Insert players
for team, players in data.SQUADS.items():
    team = session.query(Team).filter_by(name=team).first()
    players = [Player(name=p, team=team) for p in players]
    session.add_all(players)
session.commit()
# Get players by team
for team in session.query(Team).all():
    print(team.name)
    for player in team.players:
        print('\t', player.id, player.name)


# Insert leagues
leagues = [League(name=l) for l in data.LEAGUES]
session.add_all(leagues)
session.commit()

# Get leagues
for league in session.query(League).all():
    print(league.id, league.name)


# Insert matches
for match in data.MATCHES:
    home = session.query(Team).filter_by(name=match['home']).first()
    away = session.query(Team).filter_by(name=match['away']).first()
    h, a = match['score']
    date = match['date']
    league = session.query(League).filter_by(name=match['league']).first()
    match = Match(
        date=date,
        home=home,
        away=away,
        home_score=h,
        away_score=a,
        league=league)
    session.add(match)
session.commit()

# Get matches by league
for league in session.query(League).all():
    print(league.name)
    for match in league.matches:
        score = '%d x %d' % (match.home_score, match.away_score)
        print('\t', match.id, match.home.name, score, match.away.name)
