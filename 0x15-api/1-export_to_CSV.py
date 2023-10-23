#!/usr/bin/python3
"""Python script that use a given REST API
for a given employee ID, returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    u_id = eval(sys.argv[1])
    t_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(u_id)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(u_id)
    todos = requests.get(t_url).text
    user = requests.get(user_url).text

    todo_list = json.loads(todos)
    user_dict = json.loads(user)

    username = user_dict["username"]
    data = f"\"{u_id}\",\"{username}\","
    path = "{}.csv".format(sys.argv[1])
    with open(path, "w") as file:
        for elemt in todo_list:
            completed = elemt.get("completed")
            title = elemt.get("title")
            row = data + f"\"{completed}\",\"{title}\"\n"
            file.write(row)
