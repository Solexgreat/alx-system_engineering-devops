#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys

<<<<<<< HEAD
if __name__ == "__main__":
    
    user = 'users/{}'.format(sys.argv[1])
    res = requests.get('https://jsonplaceholder.typicode.com/'+ user +'')
    name = res.json().get('name')

    todo = 'todos?{}'.format(sys.argv[1])
    res = requests.get('https://jsonplaceholder.typicode.com/'+ todo +'')
    j_son = res.json()
    c_task = []
    d_task = []
    for task in j_son:
        if task.get('completed') is True and task.get('userId') == 2:
            c_task.append(task)
            d_task.append(task)
        elif task.get('completed') is False and task.get('userId') == 2:
            d_task.append(task)


    print ("Employee {} is done with task{}/{}:".format(name, len(c_task), len(d_task)))

    for keye in c_task:
        print ("\t {}".format(keye.get('title')))
=======

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    res = requests.get(user)
    json_o = res.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
>>>>>>> 1eb548dc92a1fe5b348066897419850dc3138ba5
