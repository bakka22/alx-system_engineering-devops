#!/usr/bin/python3
""" employee TODO list progress """
if __name__ == "__main__":
    import json
    import requests
    import sys

    usr_name = ""
    task_list = []
    task_count = 0
    done_count = 0
    usr_id = int(sys.argv[1])
    srch_rng = (usr_id * 20 - 19, usr_id * 20 + 1)
    for i in range(srch_rng[0], srch_rng[1]):
        url = "https://jsonplaceholder.typicode.com/todos/" + str(i)
        response = requests.get(url)
        task = response.json()
        if task.get("userId") == usr_id:
            if task.get("completed"):
                task_list.append(task.get("title"))
                done_count += 1
            task_count += 1

    url = "https://jsonplaceholder.typicode.com/users/" + str(usr_id)
    response = requests.get(url)
    usr = response.json()
    usr_name = usr.get("name")
    print(f"Employee {usr_name} is done with tasks ({done_count}/"
          + f"{task_count}):")
    for tsk in task_list:
        print(f"\t {tsk}")

