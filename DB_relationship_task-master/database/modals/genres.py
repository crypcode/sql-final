from database.database import create_table_database


def create_genres_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        genresId INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)"""
    create_table_database(query)

def create_genres_movies_table():
    query = """CREATE TABLE IF NOT EXISTS genres (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        genresId INTEGER,
                        FOREIGN KEY (genresId) REFERENCES genres(genresId),
                        moviesId INTEGER,
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId)))"""
    create_table_database(query)

create_genres_table()
create_genres_movies_table()
