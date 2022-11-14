## Importations ##


from projet_w2.InsultBlock.tweets_collect.to_json import *
from projet_w2.InsultBlock.tweets_collect.to_dataframe import *

## Programme ##


def main(username, subject):
    Tweets_1 = get_tweets_postedby(username)
    Tweets_2 = get_tweets_queries([subject])
    Tweets = Tweets_1 + Tweets_2
    nom_fichier = 'data_' + username + '_' + subject + '.json'
    to_json(Tweets, nom_fichier)
    data = to_dataframe(nom_fichier)
    return data

## Tests ##


def test_main():
    data = main("EmmanuelMacron", "agriculture")
    assert data.empty == False
    assert data['text'].empty == False
    assert type(data['text'][0]) == str

## Execution ##


if __name__ == '__main__':
    data = main("EmmanuelMacron", "agriculture")
