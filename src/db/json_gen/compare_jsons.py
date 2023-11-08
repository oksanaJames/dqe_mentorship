import json
from config import *
import mysql.connector as insert_sql
import json_rnd
from deepdiff import DeepDiff


def build_truncate_sql(db: str, table: str):
    truncate_sql = f'TRUNCATE TABLE `{db}`.`{table}`;'
    return truncate_sql


def build_json_select_query(columns: str, db: str, table: str):
    json_select_sql = f"SELECT JSON_OBJECT({columns}) as col from `{db}`.`{table}`;"
    return json_select_sql


def get_columns_from_table(db: str, table: str):
    inf_schema_sql = f"SELECT group_concat(COLUMN_NAME separator ', ') \
                    FROM INFORMATION_SCHEMA.COLUMNS \
                    WHERE TABLE_NAME = '{table}' and TABLE_SCHEMA = '{db}' \
                    order by ordinal_position;"
    return inf_schema_sql


def build_isert_sql_from_json(file_path: str, file_name: str, db: str, table: str):
    column_names = []
    column_values = []
    full_path = file_path + file_name + ".json"

    with open(full_path, encoding="utf-8", mode="r") as file:
        jsondata = json.loads(file.read())

    for key, value in jsondata.items():
        column_names.append(key)
        column_values.append(value)

    table_cols = (', '.join(column_names))
    insert_sql = f'INSERT INTO `{db}`.`{table}` ({table_cols}) VALUES {tuple(column_values)};'
    return insert_sql


if __name__ == '__main__':
    username = mysql_db['USERNAME']
    pswd = mysql_db['PASSWORD']
    hostname = mysql_db['SERVER']
    database = mysql_db['DATABASE_NEW']
    prt = mysql_db['PORT']
    table_insert_to = 'staff'
    input_path = "C:\\disk D\\Python_For_QA\\2ndEdition\\homeworks\\mentorship\\src\\db\\json_gen\\"
    output_filename = "json_for_insert"
    template_to_build_json = "json_template"

    conn = insert_sql.connect(host=hostname, user=username, passwd=pswd, db=database)

    # generate json file
    json_rnd.create_rnd_json(
        insert_file_path=input_path, # absolute file path
        insert_file_name=template_to_build_json,
        output_file_path=input_path,
        # absolute file path
        output_file_name=output_filename)

    # delete everything from the table as it has constraints
    truncate_sql = build_truncate_sql(db=database, table=table_insert_to)

    cursor = conn.cursor()
    cursor.execute(truncate_sql)
    conn.commit()
    print("Table truncated with the following statement: \n", cursor.statement, "\n", cursor.rowcount)
    print("------------------------------------------------------------------------")

    # insert data from generated json file
    insert_sql = build_isert_sql_from_json(
        file_path=input_path,
        file_name=output_filename,
        db=database, table=table_insert_to)

    cursor.execute(insert_sql)
    conn.commit()
    print("Inserted with the following statement: \n", cursor.statement, "\n", cursor.rowcount, "row(s) of data.")
    print("------------------------------------------------------------------------")

    # generate query with all columns from the table where data was inserted
    metadata_sql = get_columns_from_table(db=database, table=table_insert_to)

    cursor.execute(metadata_sql)
    myresult = cursor.fetchone()
    print("Metadata returned with the following statement: \n", cursor.statement, "\n", cursor.rowcount, "row(s) of data.")
    print("------------------------------------------------------------------------")

    # get query output and transform it to format of JSON_OBJECT() MySql function
    columns_to_select = str(myresult[0]).replace("('", "").replace("',)", "")
    columns_to_select_clean = columns_to_select.split(", ")
    columns_for_json_func = ", ".join(f"'{column}', {column}" for column in columns_to_select_clean)

    # generate sql query for select everything from table in JSON format
    select_as_json_sql = build_json_select_query(columns_for_json_func, db=database, table=table_insert_to)
    cursor.execute(select_as_json_sql)
    json_from_db = cursor.fetchone()
    print("Returned from db with the following statement: \n", cursor.statement, "\n", cursor.rowcount, "row(s) of data.")
    print("------------------------------------------------------------------------")

    # compare two JSON objects - one from file and another queries from db table
    db_result = json.loads(json_from_db[0])

    # compare two jsons - from file and from db
    with open(input_path + output_filename + ".json", encoding="utf-8", mode="r") as file:
        jsondata = json.loads(file.read())

    diff_between_file_and_db = DeepDiff(jsondata, db_result, ignore_order=True)
    print("Difference between JSON and db table:\n", diff_between_file_and_db)
