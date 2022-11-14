## Importations ##

import json
from projet_w2.InsultBlock.tweets_collect.main_collect import *

## Fonctions ##


def to_json(username, subject):
    tweets = main(username, subject, [])
    L_json = []
    for k in tweets:
        data = k._json
        L_json.append(data)
    with open("./projet_w2/InsultBlock/tweets_data/data.json", "a") as file:
        json.dump(L_json, file)

## Test ##


def test_to_json():
    to_json("EmmanuelMacron", "agriculture")
    with open("./projet_w2/InsultBlock/tweets_data/data.json", "r") as file:
        assert file.readline() != None

## Execution ##


if __name__ == '__main__':
    to_json("EmmanuelMacron", "agriculture")
