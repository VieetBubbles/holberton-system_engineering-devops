#!/usr/bin/python3

import requests


def top_ten(subreddit):
    get_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) Apple' +
        'WebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    get_object = requests.get('https://www.reddit.com/r/{:}/hot.json?limit=10'
                              .format(subreddit), headers=get_header,
                              allow_redirects=False)
    if get_object.status_code >= 300:
        print(None)

    else:
        json_to_dict = get_object.json()
        data_dictionary = json_to_dict.get('data')
        list_sorted_by_hot = data_dictionary.get('children')
        for time in list_sorted_by_hot:
            data_dict_inside = time.get('data')
            print(data_dict_inside.get('titles'))
