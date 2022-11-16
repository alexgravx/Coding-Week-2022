## Importations ##

from projet_w2.InsultBlock.insult_detector.detecteur_v1 import detecteur_v1
from projet_w2.InsultBlock.tweets_collect.to_dataframe import *

## Fonctions ##

# Import dataframe

data = to_dataframe('data_EmmanuelMacron_agriculture.json')
data = epuration_dataframe(data)


def ajout_colonnes(data):
    """
    entree: le dataframe initial
    sortie: le dataframe modifié
    """
    # Ajout de la colonne insulte
    data['insult'] = data['text'].apply(detecteur_v1)
    # Ajout de colonne 'jour' et heure
    data['jour'] = data['created_at'].apply(lambda x: x[8:10])
    data['heure'] = data['created_at'].apply(lambda x: x[11:13])
    data['mois'] = data['created_at'].apply(lambda x: x[4:7])
    return data


def stats_global(data):
    """
    # Analyse d'opinion de la plateforme. Nombres tweets qui sont des insultes et nombre qui le sont pas.
    """
    pos_twitts = len(data[data['insult'] == False].index)
    neg_twitts = len(data[data['insult'] == True].index)

# Nombre d'insultes par jour


def insult_jour(data):
    jours = data['jour'].values()
    nb_jours = len(jours)
    insulte = 0
    for jour in jours:
        insulte += len(data[data['jour'] == True].index)
    moy = insulte/nb_jours
    return moy

# Nombre d'insultes par heure


def insult_heure(data):
    heures = data['heure'].values()
    nb_heures = len(heures)
    insulte = 0
    for heure in heures:
        insulte += len(data[data['heure'] == True].index)
    moy = insulte/nb_heures
    return moy

# Statistiques par utilisateur


def insult_user(data):
    user = data['user.screen_name'].values()
    nb_users = len(user)
    moy_jour = insult_jour(data)
    moy_heure = insult_heure(data)
    return (moy_heure/nb_users, moy_jour/nb_users)
