
class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        #variables
        self.number_views = 0

    def __str__(self):
        return f"{self.title} ({self.year})" 

    def play(self):
        self.number_views += 1


class Series(Movie):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"


movie1 = Movie(title="Blade", year=1984, genre="Horror")
tv_show1 = Series(title="Friends", year=1984, genre="comedy", season_number=1, episode_number=1)

# print(movie1)
# print(tv_show1)