import csv
import random
import datetime
from wonderwords import RandomWord, RandomSentence


def generate_data_structure(file_format: dict, input_date: datetime.date, output_date: datetime.date):
    """ From the column names & column types dictionary method generates tuple
    with column names and randomly generated values
    """
    row_format = []
    for key, value in file_format.items():
        if value in ('integer', 'numeric'):
            if 'id' in key:
                row_format.append((key, i))
            else:
                row_format.append((key, random.randint(0, 100)))
        if 'decimal' in value:
            value_splitted1, value_splitted2 = value.split('(')
            dec_point, precision = value_splitted2.replace(")", "").split(",")
            row_format.append((key, round(random.uniform(1000, 2000), int(precision))))
        if value == 'string':
            if 'description' in key or 'comment' in key or 'info' in key:
                row_format.append((key, s.sentence()+s.sentence()))
            else:
                row_format.append((key, r.word(word_min_length=5, word_max_length=10)))
        if value == 'boolean':
            row_format.append((key, random.choice([True, False])))
        if value == 'date':
            random_date = input_date + (output_date - input_date) * random.random()
            row_format.append((key, str(random_date)))
        if value == 'timestamp':
            random_date = output_date - (output_date - (output_date - datetime.timedelta(days=365))) * random.random()
            random_time = random.choice([datetime.datetime.min.time(), datetime.datetime.max.time()])
            random_datetime = datetime.datetime.combine(random_date, random_time)
            row_format.append((key, random_datetime))
    return row_format


if __name__ == '__main__':
    r = RandomWord()
    s = RandomSentence()

    number_of_records = 10
    csv_format = {
        "film_id": "integer",
        "title": "string",
        "description": "string",
        "release_year": "date",
        "rental_rate": "decimal(4,2)",
        "is_active": "boolean",
        "last_update": "timestamp"}

    start = datetime.date(1980, 1, 1)
    end = datetime.date(2023, 1, 1)

    writer = csv.DictWriter(open("films.csv", "w", newline=''), fieldnames=csv_format.keys())
    writer.writerow(dict(zip(csv_format.keys(), csv_format.keys())))

    for i in range(0, number_of_records):
        row_structure = generate_data_structure(csv_format, start, end)
        writer.writerow(dict(row_structure))

