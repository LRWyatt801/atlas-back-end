#!/usr/bin/python3
"""Converts employee todo list into csv file"""

from printsurpression import SuppressPrints
from sys import argv
import csv
import importlib
API_getter = importlib.import_module('0-gather_data_from_an_API')


def json_to_csv(employee_id: int = None):
    """writes todo list to a csv file

    Args:
        employee_id (int, optional): employee id given if
            one employee's todo list is desired.
            Defaults to None.
    """
    # gets todo list
    with SuppressPrints():
        json_todo_list = API_getter.employee_todo(employee_id)

    # employee_id given
    if employee_id:
        csv_file_name = employee_id + ".csv"
    # employee_id not given
    else:
        csv_file_name = "all_user.csv"
        
    # create and write file
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in json_todo_list:
            employee_id = task.get('userId')
            username = API_getter.employee_info(employee_id, 'username')
            writer.writerow([employee_id, username,
                            task['completed'], task['title']])



if __name__ == "__main__":
    if len(argv) > 2:
        print("USAGE: python3 1-export_to_CSV.py"
              + " <employee_id: optional>")
    elif len(argv) == 1:
        json_to_csv()
    else:
        employee_id = argv[1]
        json_to_csv(employee_id)
