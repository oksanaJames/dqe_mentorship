from db_connect import *
from generate_sql import *
from config import *

driver = 'Devart ODBC Driver for MySQL'
user = mysql_db['USERNAME']
pswd = mysql_db['PASSWORD']
host = mysql_db['SERVER']
db = mysql_db['DATABASE_NEW']
prt = mysql_db['PORT']

conn = f'DRIVER={driver};User ID={user};Password={pswd};Server={host};Database={db};Port={prt};String Types=Unicode'
csv_to_sql = "films.csv"
table_to_create = "films_tbl"


def check_yourself():
    mysql_conn = Database(conn)
    file_to_insert = SqlQueries(csv_to_sql)

    header, data_types = file_to_insert.build_header_datatypes(file_to_insert.file)

    create_table_sql = file_to_insert.build_create_table_sql(header, data_types, db, table_to_create)
    insert_into_table_sql = file_to_insert.build_insert_into_table_sql(file_to_insert.file, db, table_to_create)

    mysql_conn.execute(create_table_sql)
    mysql_conn.execute(insert_into_table_sql)
    row = mysql_conn.select_query(table_to_create)
    while row:
        print(row)
        row = mysql_conn.fetchone()


if __name__ == '__main__':
    check_yourself()
