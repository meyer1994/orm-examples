import peewee as pw


db = pw.SqliteDatabase(':memory:')
# db = pw.PostgresqlDatabase('filename', user='user')
# db = pw.MySQLDatabase('filename')


class BaseModel(pw.Model):
    class Meta:
        database = db


class Team(BaseModel):
    id = pw.AutoField()
    name = pw.TextField()


class Player(BaseModel):
    id = pw.AutoField()
    name = pw.TextField()
    team = pw.ForeignKeyField(Team, backref='players')


class Match(BaseModel):
    id = pw.AutoField()
    date = pw.DateTimeField()
    home = pw.ForeignKeyField(Team, backref='matches')
    away = pw.ForeignKeyField(Team, backref='matches')
    home_score = pw.IntegerField()
    away_score = pw.IntegerField()
    league = pw.DeferredForeignKey('League', backref='matches')


class League(BaseModel):
    id = pw.AutoField()
    name = pw.TextField()



db.connect()
db.create_tables([Team, Player, Match, League])


import data

# Insert teams
for team in data.TEAMS:
    team = Team(name=team)
    team.save()

# Get teams
for team in Team.select():
    print(team.id, team.name)


# Insert players
for team, players in data.SQUADS.items():
    team = Team.get(name=team)
    for player in players:
        player = Player(name=player, team=team)
        player.save()

# Get players by team
for team in Team.select():
    print(team.name)
    for player in team.players:
        print('\t', player.id, player.name)


# Insert leagues
for league in data.LEAGUES:
    league = League(name=league)
    league.save()

# Get leagues
for league in League.select():
    print(league.id, league.name)


# Insert matches
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
    match.save()

# Get matches by league
for league in League.select():
    print(league.name)
    for match in league.matches:
        score = '%d x %d' % (match.home_score, match.away_score)
        print('\t', match.id, match.home.name, score, match.away.name)
