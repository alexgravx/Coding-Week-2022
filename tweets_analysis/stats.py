## Importations ##

from projet_w2.InsultBlock.insult_detector.detecteur_v1 import detecteur_v1
from projet_w2.InsultBlock.tweets_collect.to_dataframe import *

## Fonctions ##

data = to_dataframe('data_EmmanuelMacron_agriculture.json')
data = epuration_dataframe(data)

data['insult'] = data['text'].apply(detecteur_v1)

# Calcul du nombre de tweets

n = len(data.index)

# Analyse d'opinion de la plateforme. Nombres tweets qui sont des insultes et nombre qui le sont pas.

pos_twitts = len(data[data['insult'] == False].index)
neg_twitts = len(data[data['insult'] == True].index)
