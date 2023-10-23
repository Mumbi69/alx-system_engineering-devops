#!/usr/bin/python3
""" Gather data from an API """

import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    # Represents the URLs to fetch data from
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users/{employee_id}"
    todos_url = f"{api_url}/todos?userId={employee_id}"

    # fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # fetches todos for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # total number of tasks and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # displays the progress
    print(f"Employee {employee_name} is done with tasks\
 ({len(completed_tasks)}/{total_tasks}):")

    # displays tites of completed tasks
    for todo in todos_data:
        print(f"\t {todo['title']}")


    if __name__ == "__main__":
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
