#!/usr/bin/python3
import csv
import requests
from sys import argv


if __name__ == "__main__":
    list_of_csv_values = []

    # Get the name of the user matching the id given in the api link
    id = argv[1]
    get_userlink = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                .format(id))
    get_Name = get_userlink.json().get('username')

    # Get entire Todo json string convert to dictionary located at the api link
    Todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # Go through the dictionaries you requested
    for d in Todo:

        # Create list of values matching the userId value given
        if d.get("userId") == int(id):
            list_of_csv_values.append(["{}".format(id),
                                       "{}".format(get_Name),
                                       "{}".format(d.get("completed")),
                                       "{}".format(d.get("title"))])

    # Save dictionary values into a csv file
    with open("{}.csv".format(id), "w") as csvfile:
        spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        spamwriter.writerows(list_of_csv_values)
