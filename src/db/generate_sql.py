import csv
import ast
from dateutil.parser import parse
from datetime import datetime


class SqlQueries:
    """CSV file with header is an input. Based on header it generated CREATE TABLE statement
    for different datatypes. Based on data in CSV it generated INSERT INTO TABLE statement"""
    def __init__(self, file):
        self.file = file

    def is_date(self, text):
        try:
            parse(text)
            return True
        except ValueError:
            return False

    def is_timestamp(self, text):
        try:
            datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')
            return True
        except ValueError:
            return False

    def get_data_type(self, value_from_file, current_type):
        try:
            # Evaluates numbers to an appropriate type, and strings an error
            t = ast.literal_eval(value_from_file)
        except ValueError:
            if self.is_timestamp(value_from_file):
                return 'timestamp'
            elif self.is_date(value_from_file):
                return 'date'
            else:
                return 'varchar(100)'
        except SyntaxError:
            if self.is_timestamp(value_from_file):
                return 'timestamp'
            elif self.is_date(value_from_file):
                return 'date'
            else:
                return 'varchar(100)'

        if type(t) in [int, float]:
            if (type(t) in [int]) and current_type not in ['float', 'varchar', 'date', 'timestamp', 'boolean']:
                # Use the smallest possible int type
                if (-32768 < t < 32767) and current_type not in ['int', 'bigint']:
                    return 'smallint'
                elif (-2147483648 < t < 2147483647) and current_type not in ['bigint']:
                    return 'int'
                else:
                    return 'bigint'
        if type(t) is float and current_type not in ['varchar', 'boolean']:
            precision, scale = value_from_file.split('.')
            return f'decimal({len(precision)*2},{len(scale)})'
        elif type(t) is bool and current_type not in ['varchar']:
            return 'boolean'
        else:
            return 'varchar(100)'

    def build_header_datatypes(self, file):
        header, type_list = [], []
        with open(file, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                if len(header) == 0:
                    header = row
                    for col in row:
                        type_list.append('')
                else:
                    for i in range(len(row)):
                        # NA is the csv null value
                        if type_list[i] == 'varchar' or row[i] == 'NA':
                            pass
                        else:
                            var_type = self.get_data_type(row[i], type_list[i])
                            type_list[i] = var_type
        return header, type_list

    def build_create_table_sql(self, file_header, data_types, database_name, table_name):
        statement = f'use {database_name};\n' \
                f'drop table if exists {table_name};\n' \
                    f'create table {table_name} ('
        for i in range(len(file_header)):
            statement = (statement + '\n' + '{} {}' + ',').format(file_header[i].lower(), data_types[i])
        statement = statement[:-1] + ');'
        return statement

    def build_insert_into_table_sql(self, file, database_name, table_name):
        values = []
        with open(file, 'r') as file:
            reader = csv.reader(file)
            headers = ', '.join(next(reader))
            for row in reader:
                values.append(tuple(row))
            values_to_insert = str(values).strip('[]').replace("True", "1").replace("False", "0")
            insert_sql = f'USE {database_name};\nINSERT INTO {table_name} ({headers}) VALUES {values_to_insert};'
        return insert_sql