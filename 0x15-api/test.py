#!/usr/bin/python3
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
    if task["userId"] == usr_id:
        if task["completed"] == True:
            task_list.append(task["title"])
            done_count += 1
        task_count += 1

url = "https://jsonplaceholder.typicode.com/users/" + str(usr_id)
response = requests.get(url)
usr = response.json()
usr_name = usr["name"]
print(f"Employee {usr_name} is done with tasks ({done_count}/{task_count}):")
for tsk in task_list:
    print(f"\t {tsk}")

