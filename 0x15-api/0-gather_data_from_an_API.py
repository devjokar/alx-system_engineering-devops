#!/usr/bin/python3
""" Use JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}users/{}'.format(url, sys.argv[1])).json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = requests.get('{}todos?userId={}'.format(url, sys.argv[1])).json()
    l_task = []
    for task in todos:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(todos)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
