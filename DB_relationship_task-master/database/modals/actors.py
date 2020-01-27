from database.database import create_table_database, query_database


def create_actors_table():
    query = """CREATE TABLE IF NOT EXISTS actors (
                        actorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)


def create_actors_movies_table():
    query = """CREATE TABLE IF NOT EXISTS actors_movies (
                        actors_movies_Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        actorsId INTEGER,
                        moviesId INTEGER,
                        FOREIGN KEY (actorsId) REFERENCES actors(actorsId),
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId))"""
    create_table_database(query)


create_actors_table()
create_actors_movies_table()

query_database("PRAGMA table info(movies)")
