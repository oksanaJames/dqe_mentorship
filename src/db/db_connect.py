import pyodbc


class Database:
    """MySql databse connector and methods for queries execution"""

    def __init__(self, name):
        self._conn = pyodbc.connect(name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def select_query(self, tbl, params=None):
        self.cursor.execute(f"select * from {tbl}", params or ())
        return self.fetchall()

    def metadata_query(self, db, tbl):
        self.cursor.execute(f"SELECT group_concat(column_name order by ordinal_position separator ', ') \
        as myList FROM information_schema.columns WHERE (table_schema='{db}' and table_name = '{tbl}') \
        order by ordinal_position;")
        return self.fetchall()

    def retrieve_output(self, sql_result):
        while sql_result:
            sql_table_data = sql_result
            sql_result = self.fetchone()
        return sql_table_data

