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
    X pour les données
    y pour les labels = objectifs de valeurs à atteindre (ici des 0 ou des 1)
    """
    data = pandas.read_csv(
        '/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/train.csv', sep=',')
    data = data[['tweet', 'label']][:1000]
    X = data['tweet']
    y = data['label']
    return (X, y)


## Preprocessing ##

def preprocessing(X):

    documents = []
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(X)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(X[sen]))

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


def modèle_ML(documents, y):
    # Tri des données en mots et passage en forme lisible par l'algorithme
    vectorizer = CountVectorizer(
        max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(documents).toarray()

    # Analyse TFIDF for "Term frequency" and "Inverse Document Frequency"
    """
    Term frequency = (Number of Occurrences of a word)/(Total words in the document)
    IDF(word) = Log((Total number of documents)/(Number of documents containing the word))
    Cela permet de jauger entre la forte présence d'un mot dans un document par rapport à sa forte présence dans l'ensemble des documents
    """

    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()

    # Réparition des données dans un set d'entrainement et un set de test pour vérifier l'efficacité du modèle
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)

    # Entrainement du modèle
    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)


## Tests ##


## Evaluation du modèle ##
if __name__ == '__main__':
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    # Sauvegarde dy modèle
    with open('/Users/alexandregravereaux/Desktop/CW/projet_w2/InsultBlock/insult_detector/train_data/text_classifier', 'wb') as picklefile:
        pickle.dump(classifier, picklefile)
