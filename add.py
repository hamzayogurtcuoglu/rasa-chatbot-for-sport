from database import add_stadium

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
