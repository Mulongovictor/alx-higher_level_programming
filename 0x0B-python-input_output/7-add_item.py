#!/usr/bin/python3
""" A script that adds all arguments to a python list add saves in file of JSON representation """

if __name__ == "__main__":

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    from sys import argv

    filename = "add_item.json"

    try:
        python_list = load_from_json_file(filename)
    except FileNotFoundError:
        python_list = []

    i = 1

    for arg in argv[1:]:
        python_list.append(arg)
        i += 1

    save_to_json_file(python_list, "add_item.json")
