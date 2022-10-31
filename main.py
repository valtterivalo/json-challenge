import json
import re
from numpy import base_repr


def read_file_as_string(filename: str) -> str:
    """
    Utility function to read the contents of a file into a string
    :param filename: string representation of the name of the file we are reading
    :return: contents of the file as a single string
    """
    with open(filename) as file:
        data = file.read()
    return data


def parse_into_json(data: str) -> dict:
    """
    Utility function to parse a json string into a json object
    :param data: string of input data in readable format
    :return: map of key-value pairs parsed by the json library
    """
    json_object = json.loads(data)
    print(json_object['challenge'])
    return json_object


def format_string_for_parsing(data: str) -> str:
    """
    A brute force way to format a string to a format that allows json parsing on it - only applicable to this
    particular dataset
    :param data: input string
    :return: a string readable by most json parsers
    """
    temp_str = re.sub(r"\" ", "\", ", data)
    temp_str = re.sub(r"([a-zA-Z]*): ", r'"\1": ', temp_str)
    json_str = ''.join(('{', temp_str, '}'))
    return json_str


def encode_as_base36(number: int) -> str:
    return base_repr(number, 36)


if __name__ == '__main__':
    # Part A - do some formatting to the data and then use a built-in json parsing library to get the json object.
    data_string = read_file_as_string('event_data.txt')
    formatted_string = format_string_for_parsing(data_string)
    json_string = parse_into_json(formatted_string)

    # Part B - solve the challenge and replicate the initial data with the added, hopefully correct, fifth integer.
    # I suppose the integers are given as hex strings, and as base-36.
    print(int("0x154", 36))
    print(int("0x150", 36))
    print(int("0x14A", 36))
    print(int("0x144", 36))

    # It seems like we are first subtracting 4, then 26, then 6, and maybe 28 to get the fifth number?
    fourth_number = int("0x144", 36)
    fifth_number = fourth_number - 28
    fifth_number_as_hex = encode_as_base36(fifth_number)

    print(f"The missing number seems to be: {fifth_number}")
    print(f"As a hex string: {fifth_number_as_hex}")

    # Lastly, if I understand correctly, I am to replicate the original string here, and concatenate the missing
    # fifth number.
    data_string_final = data_string + f"five: \"{fifth_number_as_hex}\""
    print(data_string_final)
