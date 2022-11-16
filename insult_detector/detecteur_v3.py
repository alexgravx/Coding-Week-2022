## Importations ##

import pickle
import numpy as np
from projet_w2.InsultBlock.insult_detector.sklearn_entrainement import *

## Fonctions ##

X_data, y = creation_dataset('train2.csv')


def chargement(nom_modele):
    """
    charge le modèle de ML entraîné précédemment
    entrée: nom du modèle de machine learning (str)
    sortie: objets ML: modèle, réduction en vecteur et fréquencisation dans les variables "model", 'vectorizer" et "tfidfconverter"
    """
    with open('/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/' + nom_modele, 'rb') as training_model:
        model, vectorizer, tfidfconverter = pickle.load(training_model)
    return model, vectorizer, tfidfconverter


def detecteur_v3(X_data, model, vectorizer, tfidfconverter):
    """
    détecte si un set de tweets sont des insultes ou non;
    entrée: X_data, pandas.Series de tweets (chaine de caractère/str), model RandomForest entraîné, et 2 objets sklearn
    sortie: np.ndarray tq 1 pour les tweets haineux, 0 sinon (ordre conservé);
    """
    L_Tweets = preprocessing(X_data)
    X_convert = conversion_sklearn_transform(
        L_Tweets, vectorizer, tfidfconverter)
    y_result = model.predict(X_convert)
    return y_result

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
    model, vectorizer, tfidfconverter = chargement('text_classifier')
    y_result = detecteur_v3(X_data, model, vectorizer, tfidfconverter)
    print(np.where(y == 1))
