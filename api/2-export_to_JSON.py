#!/usr/bin/python3
"""exports data into json file for one employee"""
from printsurpression import SuppressPrints
import importlib
import json
from sys import argv
API_getter = importlib.import_module('0-gather_data_from_an_API')


def api_to_json_file(employee_id: int = None):
    """exports api data to a json file

    Args:
        employee_id (int, optional): employee_id to get data for one employee.
          Defaults to None.
    """
    # gets todo list
    with SuppressPrints():
        employee_info = API_getter.employee_info(employee_id)

    if employee_id:
        for user in employee_info:
            user_tasks = {}
            user_id = employee_info.get('id')
            username = employee_info.get('username')
            with SuppressPrints():
                tasks = API_getter.employee_todo(user_id)
            for task in tasks:
                task['username'] = username
            user_tasks[user_id] = tasks
    else:
        user_tasks = {}
        for user in employee_info:
            for key in user:
                user_id = user.get('id')
                username = user.get('username')
            with SuppressPrints():
                tasks = API_getter.employee_todo(user_id)
            for task in tasks:
                task['username'] = username
            user_tasks[user_id] = tasks

    # Create JSON file name
    if employee_id:
        json_file_name = employee_id + ".json"
    else:
        json_file_name = "todo_all_employees.json"

    # Create and write to file
    with open(json_file_name, mode='w') as file:
        json.dump(user_tasks, file)


if __name__ == "__main__":
    if len(argv) > 2:
        print("USAGE: python3 2-export_to_JSON.py"
              + " <employee_id>")
    elif len(argv) == 1:
        api_to_json_file()
    else:
        api_to_json_file(argv[1])