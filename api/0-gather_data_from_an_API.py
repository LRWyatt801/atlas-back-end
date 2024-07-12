#!/usr/bin/python3
"""Returns information about employees todo list"""
import requests
from sys import argv


BASE_URL = "https://jsonplaceholder.typicode.com/"


def employee_info(employee_id: int, param: str = None):
    """Retrieves employee info

    Args:
        employee_id (int): employee id
    """
    employee_url = BASE_URL + "users/{}".format(employee_id)
    if param:
        employee_info = requests.get(employee_url).json()
        employee_data = employee_info.get(param)
    else:
        employee_data = requests.get(employee_url).json()
    return employee_data


def employee_todo(employee_id: int):
    """Retrieves empyloyees todos

    Args:
        employee_id (int): employee id number
    """
    todo_url = BASE_URL + "todos/"
    employee_todos = requests.get(
        todo_url, params={'userId': employee_id}).json()

    completed_list = []
    for task in employee_todos:
        if task.get('completed'):
            completed_list.append(task)
    total_tasks = len(employee_todos)
    tasks_completed = len(completed_list)

    employee_name = employee_info(employee_id, 'name')

    print(
        "Employee {} is done with tasks {}/{}:".format(
            employee_name,
            tasks_completed,
            total_tasks)
    )
    for task in completed_list:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    employee_todo(argv[1])
