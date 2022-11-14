## Importations ##

from projet_w2.InsultBlock.tweets_collect.search_tweets import *

## Fonctions ##


def main(username, subject, Tweets):
    Tweets_1 = get_tweets_postedby(username)
    Tweets_2 = get_tweets_queries([subject])
    Tweets += Tweets_1 + Tweets_2
    return Tweets


## Test ##

def test_main():
    Tweets = []
    Tweets = main("EmmanuelMacron", "agriculture", Tweets)
    assert Tweets != None
    assert type(Tweets) == list
    assert len(Tweets) >= 0

## Execution ##


if __name__ == '__main__':
    Tweets = []
    Tweets = main("EmmanuelMacron", "agriculture", Tweets)
    print(Tweets)
