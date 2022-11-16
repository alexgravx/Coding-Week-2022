## Importations ##

import pickle
import pandas as pd
import numpy as np
from projet_w2.InsultBlock.insult_detector.sklearn_entrainement import *

## Fonctions ##


def chargement(nom_modele):
    """
    charge le modèle dans la variable "model"
    entrée: nom du modèle de machine learning (str)
    sortie: modèle de machine learning (objet RandomForest)
    """
    with open('/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/' + nom_modele, 'rb') as training_model:
        model = pickle.load(training_model)
    return model


def detecteur_v3(text, model):
    """
    détecte si un tweet est une insulte ou non
    entrée: chaine de caractère/str qui correspond au tweet, model RandomForest ou autre de ML
    sortie: 1 si c'est haineux, 0 sinon
    """
    L = pd.Series(text)
    X_test = conversion_sklearn(L)
    b = model.predict(text)
    return b

## Tests ##


def test_chargement():
    model = chargement('text_classifier')
    assert model != None


def test_detecteur_v3():
    model = chargement('text_classifier')
    b = detecteur_v3(model, 'test')
    assert type(b) == np.ndarray

## Execution ##


if __name__ == '__main__':
    test_chargement()
    #model = chargement('text_classifier')
    #b = detecteur_v3('Sandrine Rousseau messed up with his fucking politics')
    # print(b)
