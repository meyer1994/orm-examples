from itertools import chain
from datetime import datetime

from pony import orm

db = orm.Database()


class Team(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str, nullable=False)
    players = orm.Set('Player')
    home = orm.Set('Match')
    away = orm.Set('Match')

    @property
    def matches(self):
        home = (h for h in self.home)
        away = (h for h in self.away)
        return chain(home, away)


class Player(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str, nullable=False)
    team = orm.Set(Team, reverse='players')


class Match(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    date = orm.Required(datetime, nullable=False)
    home = orm.Required(Team, nullable=False, reverse='home')
    away = orm.Required(Team, nullable=False, reverse='away')
    home_score = orm.Required(int, nullable=False)
    away_score = orm.Required(int, nullable=False)
    league = orm.Set('League', reverse='matches')


class League(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    name = orm.Required(str, nullable=False)
    matches = orm.Set(Match)



db.bind(provider='sqlite', filename=':memory:', create_db=True)
# db.bind(provider='mysql', host='', user='', passwd='', db='')
# db.bind(provider='oracle', user='', password='', dsn='')
db.generate_mapping(create_tables=True)


import data

# Insert teams
with orm.db_session:
    for team in data.TEAMS:
        team = Team(name=team)

# Get teams
with orm.db_session:
    for team in Team.select():
        print(team.id, team.name)


# Insert players
with orm.db_session:
    for team, players in data.SQUADS.items():
        team = Team.get(name=team)
        for player in players:
            player = Player(name=player, team=team)

# Get players by team
with orm.db_session:
    for team in Team.select():
        print(team.name)
        for player in team.players:
            print('\t', player.id, player.name)


# Insert leagues
with orm.db_session:
    for league in data.LEAGUES:
        league = League(name=league)

# Get leagues
with orm.db_session:
    for league in League.select():
        print(league.id, league.name)


# Insert matches
with orm.db_session:
    for match in data.MATCHES:
        home = Team.get(name=match['home'])
        away = Team.get(name=match['away'])
        h, a = match['score']
        date = match['date']
        league = League.get(name=match['league'])
        match = Match(
            date=date,
            home=home,
            away=away,
            home_score=h,
            away_score=a,
            league=league)

# Get matches by league
with orm.db_session:
    for league in League.select():
        print(league.name)
        for match in league.matches:
            score = '%d x %d' % (match.home_score, match.away_score)
            print('\t', match.id, match.home.name, score, match.away.name)

# Get matches by team
with orm.db_session:
    for team in Team.select():
        print(team.name)
        for match in team.matches:
            score = '%d x %d' % (match.home_score, match.away_score)
            print('\t', match.id, match.home.name, score, match.away.name)
