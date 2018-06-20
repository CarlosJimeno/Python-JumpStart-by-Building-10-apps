import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code,title,director,keywords,duration,genres,rating,year,imdb_score')


def search_movie(search_term: str):
    if not search_term or not search_term.strip():
        raise ValueError("The search term is required")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_term)

    response = requests.get(url)
    response.raise_for_status()

    result = response.json()
    movies = [MovieResult(**mv) for mv in result.get('hits')]

    movies.sort(key=lambda m: -m.year)

    return movies


def print_movies(movies):
    for movie in movies:
        print("{} - {}".format(movie.year, movie.title))
