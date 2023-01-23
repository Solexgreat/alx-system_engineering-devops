#!/usr/bash/pyhton3

""" Script that uses JSONPlaceholder API to get information about employee """
import json
from pip._vendor import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users = '{}users'.format(url)
    req = requests.get(user)
    j_son = req.json()
    dic_task ={}
    for user in j_son:
        c = []
        userId = task.get("id") 
        todos = '{}todos?userId={}'.format(url, (userId))
        req = requests.get(todos)
        tasks = req.json()
        
        for task in tasks:
            dict_task = {"username": user.get('username'), 
                        "task": task.get('task'),
                        "completed": task.get('completed')}                
            c.append(dict_task)
        dic_task[str(userId)] = c        
filename = 'todo_all_employees.json'  
with open(filename, mode='a') as f:
    json.dump(dic_task, f)