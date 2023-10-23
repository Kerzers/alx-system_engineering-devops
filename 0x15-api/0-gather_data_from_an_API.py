#!/usr/bin/python3
"""Python script that use a given REST API
for a given employee ID, returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    count = 0
    task_count = 0
    u_id = eval(sys.argv[1])
    t_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(u_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    todos = requests.get(t_url).text
    user = requests.get(user_url).text

    todo_list = json.loads(todos)
    user_dict = json.loads(user)

    name = user_dict["name"]

    for elemt in todo_list:
        for k, v in elemt.items():
            if k == "completed" and v is True:
                task_count += 1
        count += 1
    print(f"Employee {name} is done with tasks({task_count}/{count}):")

    for elemt in todo_list:
        for k, v in elemt.items():
            if k == "completed" and v is True:
                print(f"\t {elemt['title']}")
