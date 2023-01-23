#!/usr/bash/pyhton3

""" Script that uses JSONPlaceholder API to get information about employee """
import json
from pip._vendor import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users'.format(url)
    req = requests.get(user)
    j_son = req.json()
    d ={}
    for task in j_son:
        c = []
        userId = task.get("id") 
        todo = '{}todos?userId={}'.format(url, (userId))
        req = requests.get(todo)
        j_sont = req.json()
        
        for dic in j_sont:
            dict_task = {"username": task.get('username'), 
                        "task": dic.get('task'),
                        "completed": dic.get('completed')}                
            c.append(dict_task)
        d[str(userId)] = c        
        

filename = 'todo_all_employees.json'  
with open(filename, mode='a') as f:
    json.dump(d, f)