#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    list_of_completed_tasks = []
    number_of_tasks = 0
    number_finished = 0

    # Get the name of the user matching the id given in the api link
    id = argv[1]
    get_userlink = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(id))
    get_Name = get_userlink.json().get('name')

    # Get entire Todo json string convert to dictionary located at the api link
    Todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # Go through the dictionaries you requested
    for dic in Todo:
        # Calculate the number of tasks done and the total tasks for the userId
        if dic.get("userId") == int(id) and dic.get("completed") is True:
            number_finished += 1
            number_of_tasks += 1
            list_of_completed_tasks.append(dic.get("title"))
        elif dic.get("userId") == int(id):
            number_of_tasks += 1
    print("Employee {} is done with tasks ({}/{}):"
          .format(get_Name, number_finished, number_of_tasks))
    for task in list_of_completed_tasks:
        print("\t {}".format(task))
