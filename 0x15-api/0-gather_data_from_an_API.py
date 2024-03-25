#!/usr/bin/python3
""" Todo list progress for employee """
import sys
import requests


emp_id = sys.argv[1]
request_f = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
emp_req = requests.get(request_f)

if emp_req.status_code == 200:
    resp_emp = emp_req.json()
    name = resp_emp.get('name')
    request_f = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
    todos_req = requests.get(request_f)
    if todos_req.status_code == 200:
        resp_todos = todos_req.json()
        completed_todos_count = 0
        all_c = len(resp_todos)
        completed_list = []
        for todo in resp_todos:
            if todo.get('completed'):
                completed_list.append(todo)
        completed_t_c = len(completed_list)
        print(f'Employee {name} done with tasks({completed_t_c}/{all_c}):')
        for todo in completed_list:
            print(f'\t {todo.get("title")}')
