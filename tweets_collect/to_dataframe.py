## Imports ##

import pandas as pd
import json
from pandas import json_normalize

## Fonctions ##

chemin = "./projet_w2/InsultBlock/tweets_data/"


def to_dataframe(nom_fichier):
    with open(chemin+nom_fichier, 'r', encoding='utf-8') as f:
        fichier_json = f.read()
    # Convertir le json en dictionnaire
    info = json.loads(fichier_json)
    # Normalisation
    data_json = json_normalize(info)
    # Création du dataframe à partir du dictionnaire en classant selon les colonnes
    data = pd.DataFrame.from_dict(data_json, orient='columns')
    return data

## Tests ##


def test_to_dataframe():
    data = to_dataframe('data_test.json')
    assert data["retweet_count"][0] == 3354
