import pandas as pd
from db_connect import *
from config import *
import numpy as np

driver = 'Devart ODBC Driver for MySQL'
user = mysql_db['USERNAME']
pswd = mysql_db['PASSWORD']
host = mysql_db['SERVER']
db = mysql_db['DATABASE_NEW']
prt = mysql_db['PORT']

conn = f'DRIVER={driver};User ID={user};Password={pswd};Server={host};Database={db};Port={prt};String Types=Unicode'
tbl = "films_tbl"


if __name__ == '__main__':
    mysql_conn = Database(conn)
    row = mysql_conn.select_query(tbl)
    sql_table_data = mysql_conn.retrieve_output(row)

    metadata = mysql_conn.metadata_query(db, tbl)
    tbl_columns = mysql_conn.retrieve_output(metadata)
    tbl_columns_str = [item for col in tbl_columns for item in col]
    tbl_columns_str = [item.replace(",", "") for item in tbl_columns_str[0].split()]

    sql_table_data_arr = np.array(sql_table_data)
    df = pd.DataFrame(sql_table_data_arr, columns=tbl_columns_str)

    pd.set_option('display.max_columns', None)
    # top 10 pandas methods
    print("\nhead() pandas method:")
    print(df.head())
    print("-------------------------------------")
    print("\ntail() pandas method:")
    print(df.tail())
    print("-------------------------------------")
    print("\ninfo() pandas method:")
    print(df.info())
    print("-------------------------------------")
    print("\ndtypes pandas method:")
    print(df.dtypes)
    print("-------------------------------------")
    print("\nshare and size pandas methods:")
    print(df.shape)
    print(df.size)
    print("-------------------------------------")
    print("\ndescribe() pandas method:")
    print(df.describe())
    print("-------------------------------------")
    print("\nisnull() pandas method:")
    print(df.isnull().sum())
    print("-------------------------------------")
    print("\nnunique() pandas method:")
    print(df.nunique())
    print("-------------------------------------")
    print("\nsort_index() pandas method:")
    print(df.sort_index(axis=1, ascending=True))
    print("-------------------------------------")
    print("\nquery() pandas method:")
    print(df.query("is_active == 0"))

