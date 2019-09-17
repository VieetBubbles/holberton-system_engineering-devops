#!/usr/bin/python3
import json
import requests
from sys import argv


if __name__ == "__main__":
    # Get the name of the user matching the id given in the api link
    id = argv[1]
    get_userlink = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(id))
    get_Name = get_userlink.json().get('username')

    # Get entire Todo json string convert to dictionary located at the api link
    Todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # Go through the dictionaries you requested
    json_dict = {"{}".format(id): []}
    for d in Todo:

        # Fill dictionary with keys and values matching userId
        if d.get('userId') == int(id):
            json_dict["{}"
                      .format(id)].append({"task": d.get("title"),
                                           "completed": d.get("completed"),
                                           "username": get_Name})

    # Save new dictionary into a json file
    with open("{}.json".format(id), "w") as file:
        json.dump(json_dict, file)
