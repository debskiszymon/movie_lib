import movie_lib

#helper function - 3 top titles for main output
def get_n_top_titles(library, quant=3):
    sorted_by_views = sorted(library, key=lambda e: e.number_views, reverse=True)
    for i in range(quant):
        print(f"{sorted_by_views[i].title} \nIlość wyświetleń: {sorted_by_views[i].number_views}")

#helper function for display of library
def create_full_season(Series, title, year, genre, season_number, episode_number):
    title_input = title.title()
    year_input = int(year)
    genre_input = genre.title()
    season_number_input = int(season_number)
    episode_number_input = int(episode_number)
    for i in range(1, episode_number_input + 1):
        Series(title=title_input, year=year_input, genre=genre_input, season_number=season_number_input, episode_number=i) 