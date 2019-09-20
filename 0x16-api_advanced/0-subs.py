#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    get_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    get_object = requests.get('https://www.reddit.com/r/{:}/about.json'
                              .format(subreddit), headers=get_header,
                              allow_redirects=False)
    if get_object.status_code >= 300:
        return 0

    json_to_dict = get_object.json()
    data_dictionary = json_to_dict.get('data')
    return data_dictionary.get('subscribers')
