## Importations ##

# Modules
from projet_w2.InsultBlock.insult_detector.detecteur_v1 import detecteur_v1
from projet_w2.InsultBlock.tweets_collect.to_dataframe import *


# Import dataframe
data = to_dataframe('data_missile.json')
data = epuration_dataframe(data)

data_user = to_dataframe('data_sandrousseau.json')
data_user = epuration_dataframe(data_user)

## Fonctions ##


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


data = ajout_colonnes(data)
data_user = ajout_colonnes(data_user)


def nb_insultes(data):
    """
    Analyse d'opinion de la plateforme.
    entrée: dataframe pandas data
    sortie: nombres tweets qui sont des insultes et nombre qui le sont pas type int
    """
    pas_insultes = len(data[data['insult'] == False].index)
    insultes = len(data[data['insult'] == True].index)
    total = pas_insultes + insultes
    percentage = insultes/total
    return (insultes, total, percentage)


def drop_duplicate(L):
    """
    Supprime les doublons de L
    """
    return list(set(L))


def insult_jour(data):
    """
    entrée: dataframe pandas data
    sortie: nombres moyen d'insultes par jour dans le dataframe (float)
    """
    jours = drop_duplicate(data['jour'].values)
    nb_jours = len(jours)
    insulte = 0
    for jour in jours:
        insulte += len(data[data['jour'] == True].index)
    moy = insulte/nb_jours
    return moy


def insult_heure(data):
    """
    entrée: dataframe pandas data
    sortie: nombres moyen d'insultes par heure dans le dataframe (float)
    """
    heures = drop_duplicate(data['heure'].values)
    nb_heures = len(heures)
    insulte = 0
    for heure in heures:
        insulte += len(data[data['heure'] == True].index)
    moy = insulte/nb_heures
    return moy


def max_insultes(data):
    users = drop_duplicate(data['user.screen_name'].values)
    insulte_max = 0
    for user in users:
        nb_insulte = len(data[data['user.screen_name'] == user].index)
        if nb_insulte > insulte_max:
            insulte_max = nb_insulte
    return insulte_max


# Statistiques par utilisateur


def nb_user_insult(user_data):
    """
    entrée: dataframe des tweets d'un seul utilisateur
    sortie: nombre d'insultes total de l'user (int) + nb insultes moyen par jour (float)
    """
    nb_insultes = sum(user_data['insult'])
    moy_jour = insult_jour(user_data)
    return (nb_insultes, moy_jour)


def moy_insult_user(data):
    """
    entrée: dataframe des tweets
    sortie: nb d'insultes moy/heure/user, nb insultes moy/jour/user
    """
    users = drop_duplicate(data['user.screen_name'].values)
    nb_users = len(users)
    moy_user = nb_insultes(data)[0]/nb_users
    moy_jour = insult_jour(data)
    moy_heure = insult_heure(data)
    return (moy_user, moy_heure/nb_users, moy_jour/nb_users)


## Tests ##

def test_nb_insultes():
    nb_insultes = nb_insultes(data)
    assert type(nb_insultes) == int


def test_insult_jour():
    moy = insult_jour(data)
    assert type(moy) == float


def test_max_insultes():
    moy = moy_insult_user(data)
    max = max_insultes(data)
    assert type(moy) == float
    assert type(max) == int
    assert max >= moy
