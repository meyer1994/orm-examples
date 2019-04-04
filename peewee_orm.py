import peewee as pw


db = pw.SqliteDatabase(':memory:')


class Team(pw.Model):
    name = pw.CharField()

    class Meta:
        database = db


class Match(pw.Model):
    date = pw.DateField()
    home = pw.ForeignKeyField(Team)
    away = pw.ForeignKeyField(Team)

    class Meta:
        database = db


db.connect()
db.create_tables([Team, Match])


from data import matches

for match in matches:
    home = Team(name=match['home'])
    away = Team(name=match['away'])
    match = Match(date=match['date'], home=home, away=away)

    # Save it
    home.save()
    away.save()
    match.save()


# Get single match
team = Team.get(Team.name == 'Gremio FBPA')
match = Match.get(Match.home == team)
print(match)  # 2


# Get all matches
matches = Match.select()
print(list(matches))  #  [<Match: 1>, <Match: 2>]

