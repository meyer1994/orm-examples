from datetime import datetime

from pony import orm

db = orm.Database()

class Team(db.Entity):
    name = orm.Required(str, nullable=False)
    away = orm.Set('Match')
    home = orm.Set('Match')

class Match(db.Entity):
    date = orm.Required(datetime, nullable=False)
    home = orm.Required(Team, nullable=False, reverse='home')
    away = orm.Required(Team, nullable=False, reverse='away')


db.bind(provider='sqlite', filename=':memory:', create_db=True)
db.generate_mapping(create_tables=True)


from data import matches

for match in matches:
    with orm.db_session:
        home = Team(name=match['home'])
        away = Team(name=match['away'])
        match = Match(date=match['date'], home=home, away=away)


# Get single match
with orm.db_session:
    team = Team.get(name='Gremio FBPA')
    match = Match.get(home=team)
    print(match)  # Match[2]


# Get all matches
with orm.db_session:
    matches = [m for m in Match.select()]
    print(matches)  # [Match[1], Match[2]]
