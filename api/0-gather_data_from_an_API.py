#!/usr/bin/python3
"""Retrieve information on employee and their todo list"""
import requests
from sys import argv


BASE_URL = "https://jsonplaceholder.typicode.com/"


def employee_info(employee_id: int = None, param: str = None):
    """Retrieves employee info

    Args:
        employee_id (int): employee id
    """
    if employee_id:
        employee_url = BASE_URL + "users/{}".format(employee_id)
    else:
        employee_url = BASE_URL + "users/"
    if param:
        employee_info = requests.get(employee_url).json()
        employee_data = employee_info.get(param)
    else:
        employee_data = requests.get(employee_url).json()
    return employee_data


def employee_todo(employee_id: int = None):
    """Retrieves todos

    Args:
        employee_id (int, optional): employee id number,
            defaults to None
    """
    # build url
    todo_url = BASE_URL + "todos/"
    # employee id given retrieve employee's todo list
    if employee_id:
        # Get the todo tasks for one employee
        employee_todos = requests.get(
            todo_url, params={'userId': employee_id}).json()

        # Counts the number of completed tasks / total tasks
        completed_list = []
        for task in employee_todos:
            if task.get('completed'):
                completed_list.append(task)
        total_tasks = len(employee_todos)
        tasks_completed = len(completed_list)

        employee_name = employee_info(employee_id, 'name')

        print(
            "Employee {} is done with tasks({}/{}):".format(
                employee_name,
                tasks_completed,
                total_tasks)
        )
        # print completed tasks
        for task in completed_list:
            print("\t {}".format(task.get('title')))

        # Return json of all the employee's todo list
        return employee_todos
    

    # Get the todo tasks for all employees
    employee_todos = requests.get(todo_url).json()
    return employee_todos


if __name__ == "__main__":
    if len(argv) > 2:
        print("USAGE: python3 0-gather_data_from_an_api.py"
              + " <employee_id: optional>")
    elif len(argv) == 1:
        employee_todo()
    else:
        employee_id = argv[1]
        employee_todo(employee_id)