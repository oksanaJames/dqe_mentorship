from config import *
import mysql.connector as sql


conn = sql.connect(host=mysql_db['SERVER'], user=mysql_db['USERNAME'], passwd=mysql_db['PASSWORD'], db=mysql_db['DATABASE'])


if __name__ == '__main__':
    cursor = conn.cursor()
    # Create database and tables
    with open('create_tables.sql', encoding="utf8") as f:
        for result in cursor.execute(f.read(), multi=True):
            if result.with_rows:
                print("Rows produced by statement '{}':".format(result.statement))
                for item in result.fetchall():
                    print(item)
            else:
                print("Number of rows affected by statement '{}': {}".format(
                    result.statement, result.rowcount))

    print("------------------------------------------------------------------------")
    # Populate tables with data
    with open('populate_tables.sql', 'rb') as l:
        for result in cursor.execute(l.read(), multi=True):
            if result.with_rows:
                print(f"Rows produced by statement {result.statement}:")
                for item in result.fetchall():
                    print(item)
            else:
                print(f"Number of rows affected by statement {result.statement}: {result.rowcount}")

    print("------------------------------------------------------------------------")
    # Execute queries on a data
    with open('query_tables.sql', 'rb') as m:
        for result in cursor.execute(m.read(), multi=True):
            if result.with_rows:
                print(f"\nRows produced by statement: \n{result.statement}\n")
                for item in result.fetchall():
                    print(item)
            else:
                print(f"\nNumber of rows affected by statement {result.statement}: {result.rowcount}")

    print("------------------------------------------------------------------------")
    # DELETE from table, DROP table
    with open('drop_delete.sql', 'rb') as m:
        for result in cursor.execute(m.read(), multi=True):
            if result.with_rows:
                print(f"\nRows produced by statement: \n{result.statement}\n")
                for item in result.fetchall():
                    print(item)
            else:
                print(f"\nNumber of rows affected by statement {result.statement}: {result.rowcount}")