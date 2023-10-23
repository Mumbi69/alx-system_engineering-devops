#!/usr/bin/python3
"""export data in the JSON format."""

import csv
import json
import requests
from sys import argv


def get_all_empolyee_tasks():
    # Represents the URLs to fetch data from
    api_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{api_url}/users"
    todos_url = f"{api_url}/todos"

    # fetch user information
    user_response = requests.get(user_url)
    users_data = user_response.json()

    # fetch todos for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Organizes data
    organized_data = {user["id"]: [] for user in users_data}

    for todo in todos_data:
        user_id = todo["userId"]
        username = users_data[user_id - 1]["username"]
        task_info = {
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        }
        organized_data[user_id].append(task_info)

    with open(f"todo_all_employees.json", "w") as file:
        json.dump(organized_data, file)


if __name__ == '__main__':
    get_all_empolyee_tasks()
