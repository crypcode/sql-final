from database.database import create_table_database


def create_directors_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        directorsId INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT)"""
    create_table_database(query)

def create_directors_movie_table():
    query = """CREATE TABLE IF NOT EXISTS directors (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        moviesId INTEGER,
                        FOREIGN KEY (moviesId) REFERENCES movies(moviesId),
                        directorsId INTEGER
                        FOREIGN KEY (directorsId) REFERENCES directors(directorsId))"""
    create_table_database(query)

create_directors_table()
create_directors_movie_table()

