## Importations ##

import pickle
import pandas as pd
import numpy as np
from projet_w2.InsultBlock.insult_detector.sklearn_entrainement import *

## Fonctions ##

X_data, y = creation_dataset('train2.csv')


def chargement(nom_modele):
    """
    charge le modèle dans la variable "model"
    entrée: nom du modèle de machine learning (str)
    sortie: modèle de machine learning (objet RandomForest)
    """
    with open('/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/' + nom_modele, 'rb') as training_model:
        model = pickle.load(training_model)
    return model


def detecteur_v3(X_data, model):
    """
    détecte si un tweet est une insulte ou non
    entrée: chaine de caractère/str qui correspond au tweet, model RandomForest ou autre de ML
    sortie: 1 si c'est haineux, 0 sinon
    """
    L = preprocessing(X_data)
    X_test = conversion_sklearn(L, 5, 0.7)
    X_test = X_test[:, :1123]
    b = model.predict(X_test)
    return b

## Tests ##


def test_chargement():
    model = chargement('text_classifier')
    assert model != None


def test_detecteur_v3():
    model = chargement('text_classifier')
    b = detecteur_v3(X_data, model)
    assert type(b) == np.ndarray

## Execution ##


if __name__ == '__main__':
    model = chargement('text_classifier')
    b = detecteur_v3(X_data, model)
    print(b)
    print(np.where(b == 1))
