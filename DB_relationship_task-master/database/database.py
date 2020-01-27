import sqlite3


def open_connection():
    connection = sqlite3.connect("moviesData.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def query_database(query, params=None, fetch=False):
    try:
        connection, cursor = open_connection()
        if params:
            if fetch
              for row in cursor.execute(query, params)
                print(row)
            else:
                cursor.execute(query, params)
                connection.commit()
        else:
            cursor.execute(query)
            data = cursor.fetchall
            print(data)
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


def create_table_database(query):
    try:
        connection, cursor = open_connection()
        cursor.execute(query)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()
