import random
import datetime 

#Movies Class
class Movie():

    #Movie and Series Registry
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

    #Add provided number to views
    def play(self, number):
        self.number_views += number

    def __repr__(self):
        return f"{self.title} {self.year} {self.genre}"

#TV series class
class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

    #episode counting method
    def count_episodes(self):
        count = 0
        for _ in range(self.episode_number):
            count += 1
        print(count)

#retrieves movies list
def get_movies():
    only_movies = []
    for i in Movie.registry:
        if type(i) == type(movie1):
            only_movies.append(i)
            only_movies = sorted(only_movies, key=lambda e: e.title.lower())
    return only_movies

#retrieves series list
def get_series():
    only_series = []
    for i in Movie.registry:
        if type(i) == type(tv_show1):
            only_series.append(i)
            only_series = sorted(only_series, key=lambda e: e.title.lower())
    return only_series

#search function, prompts a input, returns all movies or series that match the input 
def search():
    search_query = input("podaj: ").lower()
    for i in Movie.registry:
        if i.title.lower() == search_query:
            print(i)

#generate views for 1 to 100 for a random title
def generate_views():
    random_item = random.choice(Movie.registry)
    x = random.randint(1,101)
    random_item.play(x) 
    return f"{random_item.title} {random_item.number_views}"

#generate views randomly ten times
def ten_times():
    for _ in range(10): generate_views()

#retrieves top titles from series or movies depending on prompt
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

#helper function - 3 top titles for main output
def top_titles_automatic():
    quant = 3
    sorted_by_views = sorted(Movie.registry, key=lambda e: e.number_views, reverse=True)
    for i in range(quant):
        print(f"{sorted_by_views[i].title} \nIlość wyświetleń: {sorted_by_views[i].number_views}")

#adds full season of episodes based on prompt
def full_season(Series):
    title_input = input("Podaj tytuł: ").title()
    year_input = int(input("Podaj rok wydania: "))
    genre_input = input("Podaj gatunek: ").title()
    season_number_input = int(input("Podaj sezon: "))
    episode_number_input = int(input("Podaj ilość odćinków: "))
    for i in range(episode_number_input + 1):
        Series(title=title_input, year=year_input, genre=genre_input, season_number=season_number_input, episode_number=i) 

#helper function for display of library
def full_season_automatic(Series, title, year, genre, season_number, episode_number):
    title_input = title.title()
    year_input = int(year)
    genre_input = genre.title()
    season_number_input = int(season_number)
    episode_number_input = int(episode_number)
    for i in range(1, episode_number_input + 1):
        Series(title=title_input, year=year_input, genre=genre_input, season_number=season_number_input, episode_number=i) 



if __name__ == "__main__":
    #library
    full_season_automatic(Series, "friends", 1990, "comedy", 5, 6)
    full_season_automatic(Series, "How I Met Your Mother", 1984, "comedy", 1, 6)
    movie1 = Movie(title="Blade", year=1984, genre="Horror")
    movie2 = Movie(title="Titanic", year=1984, genre="Horror")
    movie3 = Movie(title="A Nightmare on Elm Street", year=1984, genre="Horror")
    movie4 = Movie(title="A League of Their Own", year=1984, genre="Horror")
    tv_show1 = Series(title="Friends", year=1984, genre="comedy", season_number=1, episode_number=1)
    tv_show2 = Series(title="Big Bang Theory", year=1984, genre="comedy", season_number=1, episode_number=1)

    print("Biblioteka Filmów:")
    print("------------------")
    print("Filmy:\n")
    for movie in get_movies():
        print(movie)
    # print("---------")
    print("\nSeriale:\n")
    for series in get_series():
        print(series)
    
    ten_times()
    today = datetime.datetime.now().strftime("%d.%m.%Y")
    # print("---------")
    print(f"\nNajpopularniejsze filmy i seriale dnia {today}:\n")
    
    top_titles_automatic()

# print(Movie.registry)

# search()

# full_season(Series)

# print(ten_times())

# top_titles()

# tv_show1.count_episodes()

