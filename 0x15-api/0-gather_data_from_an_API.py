#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

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
