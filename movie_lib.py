import random


class Movie():

    registry = []

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.registry.append(self)

        #variables
        self.number_views = 0
        
    def __str__(self):
        return f"{self.title} ({self.year})" 

    def play(self, number):
        self.number_views += number

    def __repr__(self):
        return f"{self.title}{self.year}{self.genre}"


class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

     

def get_movies():
    only_movies = []
    for i in Movie.registry:
        if type(i) == type(movie1):
            only_movies.append(i)
            only_movies = sorted(only_movies, key=lambda e: e.title.lower())
    return only_movies

def get_series():
    only_series = []
    for i in Movie.registry:
        if type(i) == type(tv_show1):
            only_series.append(i)
            only_series = sorted(only_series, key=lambda e: e.title.lower())
    return only_series

def search():
    search_query = input("podaj: ").lower()
    for i in Movie.registry:
        if i.title.lower() == search_query:
            print(i.title)

def generate_views():
    random_item = random.choice(Movie.registry)
    x = random.randint(1,101)
    random_item.play(x) 
    return f"{random_item.title} {random_item.number_views}"

def ten_times():
    for _ in range(10): generate_views()

def top_titles():
    ten_times()
    quant = int(input("Podaj ilość: "))
    content_type = input("Serial czy film? ").lower()
    if content_type == "film":
        sorted_by_views = sorted(get_movies(), key=lambda e: e.number_views, reverse=True)
        for i in range(quant):
            print(f"{sorted_by_views[i].title} {sorted_by_views[i].number_views}")
    elif content_type == "serial":
        sorted_by_views = sorted(get_series(), key=lambda e: e.number_views, reverse=True)
        for i in range(quant):
            print(f"{sorted_by_views[i].title} {sorted_by_views[i].number_views}")


movie1 = Movie(title="Blade", year=1984, genre="Horror")
movie2 = Movie(title="Titanic", year=1984, genre="Horror")
movie3 = Movie(title="A Nightmare on Elm Street", year=1984, genre="Horror")
movie4 = Movie(title="A League of Their Own", year=1984, genre="Horror")
tv_show1 = Series(title="Friends", year=1984, genre="comedy", season_number=1, episode_number=1)
tv_show1 = Series(title="Big Bang Theory", year=1984, genre="comedy", season_number=1, episode_number=1)
tv_show1 = Series(title="How I Met Your Mother", year=1984, genre="comedy", season_number=1, episode_number=1)

# search()

# print(get_movies())
# print("---------")
# print(get_series())

# generate_views()

# print(ten_times())

# top_titles()
