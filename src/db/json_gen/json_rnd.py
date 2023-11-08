import json
import random
import string
from src.db.json_gen.json_keys_dict import JsonKeys


def convert_json_into_var(file_path: str, file_name: str):
    with open(file_path + file_name + ".json", encoding="utf8") as json_file:
        return json.load(json_file)


def convert_var_into_json(
        file_path: str, file_name: str, json_var):
    with open(file_path + file_name + ".json", encoding="utf8", mode="w") as json_file:
        return json_file.write(json.dumps(json_var))


def generate_str_row(qty):
    str_output = ""
    for i in range(qty):
        str_output += random.choice(string.ascii_letters)
    return str_output


def create_rnd_json(insert_file_path, insert_file_name, output_file_path, output_file_name):
    insert_json = convert_json_into_var(file_path=insert_file_path, file_name=insert_file_name)
    # print(type(insert_json))
    output_dict = {}
    for key in insert_json.keys():
        # print(key)
        if key == JsonKeys.ID.value:
            val = random.randint(0, 100)
        elif key == JsonKeys.EMAIL.value:
            val = generate_str_row(10) + "@" + \
                  generate_str_row(4) + "." + \
                  generate_str_row(3)
        elif key == JsonKeys.STORE.value:
            val = random.randint(0, 2)
        elif key == JsonKeys.ADDRESS.value:
            val = random.randint(0, 20)
        elif key == JsonKeys.IS_ACTIVE.value:
            val = random.randint(0, 1)
        elif key == JsonKeys.FIRST_NAME.value:
            val = generate_str_row(7)
        elif key == JsonKeys.LAST_NAME.value:
            val = generate_str_row(9)
        elif key == JsonKeys.USER_NAME.value:
            val = generate_str_row(15)
        elif key == JsonKeys.PASSWORD.value:
            val = generate_str_row(12)
        else:
            val = ""
        output_dict[key] = val
    convert_var_into_json(
        file_path=output_file_path,
        file_name=output_file_name,
        json_var=output_dict)


# create_rnd_json(
#     insert_file_path="C:\\disk D\\Python_For_QA\\2ndEdition\\homeworks\\mentorship\\src\\db\\json_gen\\",  # absolute file path
#     insert_file_name="json_template",
#     output_file_path="C:\\disk D\\Python_For_QA\\2ndEdition\\homeworks\\mentorship\\src\\db\\json_gen\\",  # absolute file path
#     output_file_name="new_json_file")

