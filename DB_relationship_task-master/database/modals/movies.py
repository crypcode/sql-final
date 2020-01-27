from database.database import create_table_database, query_database
from entities.movie import Movie


def create_movies_table():
    query = """CREATE TABLE IF NOT EXISTS movies (
                        moviesId INTEGER PRIMARY KEY AUTOINCREMENT,
                        movie_name TEXT,
                        release_date DATE,
                        rating REAL,
                        genre TEXT,
                        studioId INTEGER,
                        boxofficeId INTEGER,
                        FOREIGN KEY (studioId) REFERENCES studios(studioId),
                        FOREIGN KEY (boxofficeId) REFERENCES box_offices(boxofficeId))"""

    create_table_database(query)
# Isspausdina lentele
# query_database("PRAGMA table_info(movies)")

# Dropina lentele
# create_table_database("DROP TABLE movies")
# create_movies_table()

def create_movie(Movie):
    query = """INSERT INTO movies VALUES (?, ?, ?, ? ,? ,?, ?)"""
    params = (Movie.moviesId, Movie.movie_name, Movie.release_date, Movie.rating, Movie.genre,
              Movie.studioId, Movie.boxofficeId)
    query_database(query, params)

Movie1 = Movie(None, 'Boratas' , 2008, 8, 'Komedija',
              None, None)
create_movie(Movie1)

def get_movie(Movie):
    query = """SELECT * FROM movies WHERE moviesId = (?) OR movie_name = (?) OR release_date = (?)
     OR rating = (?) OR genre = (?) OR studioId = (?) OR boxofficeId = (?)"""
    params = (Movie.moviesId, Movie.movie_name, Movie.release_date, Movie.rating, Movie.genre, Movie.studioId,
              Movie.boxofficeId)
    query_database(query, params, True)

get_movie(Movie1)