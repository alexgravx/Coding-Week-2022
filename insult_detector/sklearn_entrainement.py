## Importations ##


# Modules
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pickle
import pandas
import numpy as np
import re
import nltk
from sklearn.datasets import load_files

# dataset


def creation_dataset():
    """
    retourne deux arrays sklearn
    X pour les données (type pandas.Series)
    y pour les labels = objectifs de valeurs à atteindre: 1 si insulte et 0 sinon) (type pandas.Series)
    """
    data = pandas.read_csv(
        '/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/train.csv', sep=',')
    data = data[['tweet', 'label']][:4000]
    X_data = data['tweet']
    y = data['label']
    return (X_data, y)


## Preprocessing ##

def preprocessing(X_data):
    """
    entrée: pandas.Series qui regroupe l'ensemble des tweets classés dans le même ordre que leur label dans y
    sortie: documents est une liste des tweets lemmatizés et classés selon le même ordre qu'au début
    """

    documents = []
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X_data)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X_data[sen]))
        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        # Removing prefixed 'b' (cas lecture des documents)
        document = re.sub(r'^b\s+', '', document)
        # Converting to Lowercase
        document = document.lower()
        # Lemmatization
        document = document.split()
        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)
        documents.append(document)
    return documents

## Creation du modèle de ML ##


def conversion_sklearn(documents):
    """
    entrée: documents, liste des tweets lemmatizés et classés selon le même ordre qu'au début;
    sortie: X, tableau numpy np.ndarray converti pour sklearn (tableaux de nombres);
    """
    # Tri des données en mots et passage en forme lisible par l'algorithme
    vectorizer = CountVectorizer(
        max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(documents).toarray()

    # Analyse TFIDF for "Term frequency" and "Inverse Document Frequency"
    # Term frequency = (Number of Occurrences of a word)/(Total words in the document)
    # IDF(word) = Log((Total number of documents)/(Number of documents containing the word))
    # Cela permet de jauger entre la forte présence d'un mot dans un document par rapport à sa forte présence dans l'ensemble des documents
    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()
    return X


def decoupage_dataset(X, y):
    """
    Réparition des données dans un set d'entrainement et un set de test pour vérifier l'efficacité du modèle
    entrée: X, np.ndarray fourni par la fonction conversion_sklearn; y, pandas.Series des labels (valeurs 0 ou 1) et indique si les tweets sont insultants(1) ou non (0)
    sortie: X et y découpés chacun un deux sous tableaux numpy et pandas.Series (respectivempent) d'entrainement et de test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)
    return (X_train, X_test, y_train, y_test)


def entrainement_modele(X_train, y_train):
    """
    Entrainement du modèle
    entrée: tableaux numpy X_train et y_train issus du découpage des tableaux précédents.
    sortie: objet RandomForest, capable d'analyser si un tweet est haineux ou non par la méthode objet.predict(tweet)
    Remarque: y_test est un pandas.Series et y_pred issus de classifier.predict(X_test) est un np.ndarray
    """
    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)
    return classifier


## Tests ##

def test_creation_dataframe():
    X_data, y = creation_dataset()
    assert type(X_data) == pandas.Series
    assert type(y) == pandas.Series
    assert 0 in y
    assert 1 in y


def test_preprocessing():
    X_data, y = creation_dataset()
    documents = preprocessing(X_data)
    assert type(documents) == list
    assert type(documents[0]) == str


def test_conversion_sklearn():
    X_data, y = creation_dataset()
    documents = preprocessing(X_data)
    X = conversion_sklearn(documents)
    assert type(X) == np.ndarray


def test_decoupage():
    X_data, y = creation_dataset()
    documents = preprocessing(X_data)
    X = conversion_sklearn(documents)
    X_train, X_test, y_train, y_test = decoupage_dataset(X, y)
    assert type(X_train) == np.ndarray
    assert type(X_test) == np.ndarray
    assert type(y_train) == pandas.Series
    assert type(y_test) == pandas.Series


## Evaluation du modèle ##

if __name__ == '__main__':

    # Creation du modèle de ML
    print("*Creation du dataset en cours* \n")
    X, y = creation_dataset()
    print("*Preprocessing en cours* \n")
    documents = preprocessing(X)
    print("*Creation du modèle en cours* \n")
    X = conversion_sklearn(documents)
    X_train, X_test, y_train, y_test = decoupage_dataset(X, y)
    classifier = entrainement_modele(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # Affichage des matrices d'efficacité du modèle
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    # Sauvegarde dy modèle
    with open('/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/text_classifier', 'wb') as picklefile:
        pickle.dump(classifier, picklefile)
