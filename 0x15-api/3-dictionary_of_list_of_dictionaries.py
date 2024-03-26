#!/usr/bin/python3
""" employee TODO list progress """
if __name__ == "__main__":
    import json
    import requests
    import sys

    task_dic = {}
    path = "todo_all_employees.json"

    for usr_id in range(1, 11):

        usr_name = ""
        srch_rng = (usr_id * 20 - 19, usr_id * 20 + 1)
        task_dic[str(usr_id)] = []
        url = "https://jsonplaceholder.typicode.com/users/" +\
            str(usr_id)
        response = requests.get(url)
        usr = response.json()
        usr_name = usr.get("username")

        for i in range(srch_rng[0], srch_rng[1]):

            url = "https://jsonplaceholder.typicode.com/todos/" + str(i)
            response = requests.get(url)
            task = response.json()
            if task.get("userId") == usr_id:
                tmp = {}
                tmp["task"] = task.get("title")
                tmp["completed"] = task.get("completed")
                tmp["username"] = usr_name
                task_dic[str(usr_id)].append(tmp)

    with open(path, "w") as f:
        json.dump(task_dic, f)
