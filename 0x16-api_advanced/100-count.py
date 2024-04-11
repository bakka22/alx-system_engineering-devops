#!/usr/bin/python3
"""  parses the title of all hot articles, and prints a sorted count
of given keywords """


import requests


def count_words(subreddit, word_list, after=None, word_dic=None, counter=0):
    """  parses the title of all hot articles, and prints a sorted coun
    of given keywords"""
    if word_list == []:
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit API Client"}
    if word_dic is None:
        word_dic = {}
        for index, word in enumerate(word_list):
            if word_dic.get(word.lower()) is None:
                word_dic[word.lower()] = {"count": 0, "multi": 0}
            for word2 in word_list:
                if word == word2.lower():
                    if word_dic.get(word) is not None:
                        word_dic[word]['multi'] += 1
    if after:
        params = {
                "limit": 100,
                "after": after
        }
    else:
        params = {
               "limit": 100,
        }
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    after = data.get('data').get('after')
    hot = data.get('data').get('children')
    for post in hot:
        for title_word in post.get('data').get('title').split():
            if word_dic.get(title_word.lower()) is not None:
                word_dic[title_word.lower()]['count'] += 1
    if after is None:
        return
    count_words(subreddit, word_list, after, word_dic, counter+1)
    if counter == 0:
        word_dic = dict(sorted(word_dic.items(), key=lambda x: x[0]))
        word_dic = dict(sorted(word_dic.items(), key=lambda x:
                        x[1].get('count'), reverse=True))
        for key, value in word_dic.items():
            if value['count'] != 0:
                total = value['count'] * value['multi']
                print(f"{key}: {total}")
