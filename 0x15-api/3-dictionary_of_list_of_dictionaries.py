#!/usr/bin/python3
import json
import requests


if __name__ == "__main__":
    json_dict = {}
    userId = 1

    # Get entire Todo json string convert to dictionary located at the api link
    Todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # Go through the dictionaries you requested
    for d in Todo:

        # Get the correct userId to place into the json dictionary
        if d.get("userId") != userId:
            userId = d.get("userId")

        # Get the username of the user matching the id given in the api link
        get_u = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                             .format(userId))
        get_UserName = get_u.json().get('username')

        # add the correct userId to the new dictionary as the key name
        if userId not in json_dict.keys():
            json_dict[userId] = []

        # add the correct values matching the userId
        if d.get("userId") == userId:
            json_dict[userId].append({
                "username": get_UserName,
                "task": d.get("title"),
                "completed": d.get("completed")})

    # Save new dictionary into a json file
    with open("todo_all_employees.json", "w") as file:
        json.dump(json_dict, file)
