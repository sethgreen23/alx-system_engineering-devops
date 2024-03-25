#!/usr/bin/python3
""" Todo list progress for employee """

if __name__ == "__main__":
    import csv
    import requests
    import sys

    id = sys.argv[1]
    if id:
        try:
            id = int(id)
            req_f = f'https://jsonplaceholder.typicode.com/users/{id}'
            emp_req = requests.get(req_f)
            if emp_req.status_code == 200:
                resp_emp = emp_req.json()
                name = resp_emp.get('name')
                username = resp_emp.get('username')
                req_f = (
                    f'https://jsonplaceholder.typicode.com/todos?userId={id}')
                todos_req = requests.get(req_f)
                if todos_req.status_code == 200:
                    resp_todos = todos_req.json()
                    completed_todos_count = 0
                    all_c = len(resp_todos)
                    completed_list = []
                    for todo in resp_todos:
                        if todo.get('completed'):
                            completed_list.append(todo)
                    completed_t_c = len(completed_list)
                    print(f'Employee {name} is '
                          f'done with tasks({completed_t_c}/{all_c}):')
                    for todo in completed_list:
                        print(f'\t {todo.get("title")}')
                    fn = ["USER_ID",
                          "USERNAME",
                          "TASK_COMPLETED_STAT",
                          "TASK_TITLE"]
                    filename = f'{id}.csv'
                    with open(filename, mode='w') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fn)
                        # writer.writeheader()
                        for todo in resp_todos:
                            writer.writerow({
                                "USER_ID": f'{id}',
                                "USERNAME": username,
                                "TASK_COMPLETED_STAT": todo.get('completed'),
                                "TASK_TITLE": todo.get('title')
                                })
        except ValueError:
            pass
