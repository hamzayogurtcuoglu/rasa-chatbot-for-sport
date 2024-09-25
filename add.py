from database import add_stadium, add_match_scores

stadiums = [
    ("camp nou", "barcelona", 99354, "barcelona"),
    ("santiago bernabeu", "madrid", 81044, "real madrid"),
    ("old trafford", "manchester", 74879, "manchester united"),
    ("allianz arena", "munich", 75000, "bayern munich"),
    ("anfield", "liverpool", 53394, "liverpool"),
    ("stamford bridge", "london", 41837, "chelsea"),
    ("san siro", "milan", 80018, "ac milan"),
    ("emirates stadium", "london", 60260, "arsenal"),
    ("signal iduna park", "dortmund", 81365, "borussia dortmund"),
    ("parc des princes", "paris", 47929, "paris saint-germain"),
    ("juventus stadium", "turin", 41507, "juventus"),
    ("wanda metropolitano", "madrid", 68456, "atletico madrid"),
    ("tottenham hotspur stadium", "london", 62850, "tottenham hotspur"),
    ("estadio do dragao", "porto", 50033, "porto"),
    ("estadio da luz", "lisbon", 64642, "benfica"),
    ("celtic park", "glasgow", 60832, "celtic"),
    ("ibrox stadium", "glasgow", 50817, "rangers"),
    ("amsterdam arena", "amsterdam", 54990, "ajax"),
    ("de kuip", "rotterdam", 51117, "feyenoord"),
    ("estadio mestalla", "valencia", 55000, "valencia"),
    ("olympiastadion", "berlin", 74475, "hertha berlin"),
    ("stade velodrome", "marseille", 67000, "marseille"),
    ("etihad stadium", "manchester", 55017, "manchester city"),
    ("stadio olimpico", "rome", 70634, "as roma"),
    ("estadio monumental", "buenos aires", 70074, "river plate"),
    ("la bombonera", "buenos aires", 49000, "boca juniors"),
    ("maracana stadium", "rio de janeiro", 78838, "flamengo"),
    ("turk telekom arena", "istanbul", 52650, "galatasaray"),
    ("vodafone park", "istanbul", 41903, "besiktas"),
    ("sukru saracoglu stadium", "istanbul", 50530, "fenerbahce")
]

# Stadyumları eklemek
for stadium in stadiums:
    add_stadium(*stadium)


# 30 farklı match eklemek
add_match_scores("barcelona", "real madrid", 2, 1, "messi", "benzema")
add_match_scores("manchester united", "chelsea", 3, 2, "rashford, fernandes", "havertz")
add_match_scores("liverpool", "manchester city", 1, 1, "salah", "de bruyne")
add_match_scores("juventus", "ac milan", 2, 2, "ronaldo, dybala", "ibrahimovic, leao")
add_match_scores("psg", "lyon", 3, 0, "mbappe, neymar, di maria", "none")
add_match_scores("bayern munich", "borussia dortmund", 4, 1, "lewandowski, gnabry, sané", "haaland")
add_match_scores("inter", "napoli", 1, 0, "lukaku", "none")
add_match_scores("arsenal", "tottenham", 2, 1, "aubameyang, lacazette", "kane")
add_match_scores("roma", "lazio", 3, 2, "dzeko, pellegrini", "immobile, savic")
add_match_scores("sevilla", "valencia", 1, 1, "ocampos", "gaya")
add_match_scores("ajax", "feyenoord", 2, 0, "tadic, haller", "none")
add_match_scores("porto", "benfica", 1, 3, "otavio", "darwin nunez, rafa silva")
add_match_scores("atletico madrid", "barcelona", 0, 1, "none", "messi")
add_match_scores("real sociedad", "villareal", 2, 2, "oyarzabal, isak", "gerard moreno, parejo")
add_match_scores("marseille", "monaco", 1, 1, "payet", "ben yedder")
add_match_scores("celtic", "rangers", 0, 2, "none", "kent, morelos")
add_match_scores("galatasaray", "fenerbahce", 1, 1, "feghouli", "valencia")
add_match_scores("besiktas", "trabzonspor", 3, 1, "ghezzal, hutchinson", "bakasetas")
add_match_scores("leipzig", "bayer leverkusen", 2, 2, "nkunku, forsberg", "schick, diaby")
add_match_scores("tottenham", "west ham", 3, 3, "kane, son", "antonio, bowen")
add_match_scores("everton", "leeds united", 2, 0, "richarlison, calvert-lewin", "none")
add_match_scores("wolves", "aston villa", 1, 1, "neto", "watkins")
add_match_scores("leicester city", "newcastle", 1, 2, "vardy", "wilson, almiron")
add_match_scores("burnley", "sheffield united", 0, 1, "none", "mcgoldrick")
add_match_scores("southampton", "brighton", 1, 1, "ings", "trossard")
add_match_scores("real betis", "celta vigo", 2, 3, "canales, borja iglesias", "aspas, mina, beltran")
add_match_scores("getafe", "osasuna", 1, 0, "mata", "none")
add_match_scores("granada", "mallorca", 3, 1, "molina, puertas", "kuboo")
add_match_scores("shakhtar donetsk", "dynamo kyiv", 0, 1, "none", "garmash")
add_match_scores("anderlecht", "club brugge", 2, 2, "refaelov, sardella", "lang, de ketelaere")
