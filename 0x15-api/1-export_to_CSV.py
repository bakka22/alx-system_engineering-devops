#!/usr/bin/python3
""" employee TODO list progress """
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    usr_name = ""
    task_list = []
    task_count = 0
    done_count = 0
    usr_id = int(sys.argv[1])
    file_path = str(usr_id) + ".csv"
    srch_rng = (usr_id * 20 - 19, usr_id * 20 + 1)
    url = "https://jsonplaceholder.typicode.com/users/" + str(usr_id)
    response = requests.get(url)
    usr = response.json()
    usr_name = usr.get("name")
    for i in range(srch_rng[0], srch_rng[1]):
        url = "https://jsonplaceholder.typicode.com/todos/" + str(i)
        response = requests.get(url)
        task = response.json()
        if task.get("userId") == usr_id:
            tmp = [f"{usr_id}", f"{usr_name}",
                   f"{task.get('completed')}", f"{task.get('title')}"]
            task_list.append(tmp)
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(task_list)
