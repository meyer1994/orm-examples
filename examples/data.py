from datetime import datetime


SQUADS = {
    # As of 31 January 2019, Wikipedia
    'Manchester United F.C': [
        'David de Gea',
        'Victor Lindelöf',
        'DF  Eric Bailly',
        'Phil Jones',
        'Paul Pogba',
        'Alexis Sánchez',
        'Juan Mata',
        'Romelu Lukaku',
        'Marcus Rashford',
        'Anthony Martial',
        'Chris Smalling',
        'Lee Grant',
        'Jesse Lingard',
        'Andreas Pereira',
        'Marcos Rojo',
        'Fred',
        'Ashley Young',
        'Diogo Dalot',
        'Ander Herrera',
        'Sergio Romero',
        'Luke Shaw',
        'Antonio Valencia',
        'Nemanja Matić',
        'Matteo Darmian',
        'Scott McTominay'
    ],
    # As of 13 January 2019, Wikipedia
    'Chelsea F.C': [
        'Kepa Arrizabalaga',
        'Antonio Rüdiger',
        'Marcos Alonso',
        'Jorginho',
        'Danny Drinkwater',
        "N'Golo Kanté",
        'Ross Barkley',
        'Gonzalo Higuaín',
        'Eden Hazard',
        'Pedro',
        'Ruben Loftus-Cheek',
        'Willy Caballero',
        'Mateo Kovačić',
        'Olivier Giroud',
        'Callum Hudson-Odoi',
        'Davide Zappacosta',
        'Willian',
        'Gary Cahill',
        'Andreas Christensen',
        'César Azpilicueta',
        'David Luiz',
        'Robert Green',
        'Emerson',
        'Ethan Ampadu',
        'Marco van Ginkel'
    ],
    # As of 20 March 2019, Wikipedia
    'Grêmio Foot-Ball Porto Alegrense': [
        'Paulo Victor',
        'Léo Moura',
        'Pedro Geromel',
        'Walter Kannemann',
        'Michel',
        'Leonardo Gomes',
        'Luan',
        'Maicon',
        'Diego Tardelli',
        'Felipe Vizeu',
        'Everton',
        'Bruno Cortez',
        'Rômulo',
        'Matheus Henrique',
        'Vico',
        'Thaciano',
        'Lincoln',
        'Walter Montoya',
        'Jean Pyerre',
        'Júlio César',
        'Alisson',
        'Brenno',
        'Pepê',
        'Marcelo Oliveira',
        'Thonny Anderson',
        'Paulo Miranda',
        'Juninho Capixaba',
        'Marinho',
        'Darlan Mendes',
        'Rodrigues',
        'Phelipe Megiolaro',
        'Rafael Galhardo',
        'André'
    ],
    # As of 26 March 2019, Wikipedia
    'Sociedade Esportiva Palmeiras': [
        'Fernando Prass',
        'Marcos Rocha',
        'Edu Dracena',
        'Thiago Santos',
        'Diogo',
        'Dudu',
        'Zé Rafael',
        'Miguel Borja',
        'Moisés',
        'Ricardo Goulart',
        'Mayke',
        'Luan',
        'Gustavo Scarpa',
        'Gustavo Gómez',
        'Deyverson',
        'Jean',
        'Alejandro Guerra',
        'Bruno Henrique',
        'Lucas Lima',
        'Weverton',
        'Raphael Veiga',
        'Antônio Carlos',
        'Victor Luis',
        'Felipe Pires',
        'Hyoran',
        'Willian',
        'Felipe Melo',
        'Fabiano',
        'Juninho',
        'Matheus',
        'Carlos Eduardo',
        'Arthur',
        'Jailson',
        'Luan Silva'
    ]
}

# Names taken from Wikipedia
TEAMS = [
    'Manchester United F.C',
    'Chelsea F.C',
    'Grêmio Foot-Ball Porto Alegrense',
    'Sociedade Esportiva Palmeiras'
]

# Mix of imagination and reality
LEAGUES = [
    'Premier League',
    'Other League',
    'Brasileirão'
]

# Invented by me
MATCHES = [
    {
        'home': 'Chelsea F.C',
        'away': 'Manchester United F.C',
        'score': [0, 0],
        'date': datetime.utcnow(),
        'league': 'Premier League'
    },
    {
        'home': 'Manchester United F.C',
        'away': 'Grêmio Foot-Ball Porto Alegrense',
        'score': [2, 1],
        'date': datetime.utcnow(),
        'league': 'Other League'
    },
    {
        'home': 'Sociedade Esportiva Palmeiras',
        'away': 'Chelsea F.C',
        'score': [1, 4],
        'date': datetime.utcnow(),
        'league': 'Other League'
    },
    {
        'home': 'Grêmio Foot-Ball Porto Alegrense',
        'away': 'Sociedade Esportiva Palmeiras',
        'score': [3, 2],
        'date': datetime.utcnow(),
        'league': 'Brasileirão'
    }
]
