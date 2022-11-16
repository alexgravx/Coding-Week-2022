## IMPORTS ##
import pandas as pd
from textblob import TextBlob
from textblob import Word

## DEFINITIONS ##
chemin = './projet_w2/InsultBlock/insult_detector/'
texte_fr = "Bjr mesdames, messieurs !\n je m'appelle hugues et j'aime pas les bougnouls et les fils de pute"
texte_en = "During this scene, I was hungry. Fuck you, i don't like bitches"  # v1 en anglais

# Dictionnaire des mots sémantiquement peu importants
dictionnaire_inutile_en = {"ourselves", "hers", "between", "yourself", "again", "there", "about", "once", "during", "out", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above",
                           "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}
dictionnaire_inutile_fr = {"m", "t", "s", "c", "entre", "encore", "là", "sur", "une fois", "pendant", "dehors", "avoir", "avec", "ils", "propre", "un", "être", "certains", "pour", "faire", "son", "votre", "tel", "dans", "de", "plus", "lui-même", "autre", "hors", "est", "suis", "es", "est", "sommes", "êtes", "or", "qui", "comme", "depuis", "lui", "chaque", "le", "leurs", "jusqu'à", " en dessous", "sont", "ces", "votre", "son", "à travers", "moi", "étaient", "elle", "plus", "lui-même",
                           "ce", "en bas", "devrait", "notre", "leur", "pendant", "au-dessus", "à", "notre", "avait", "avaient", "avais", "avions", "tout", "où", "avant", "eux",  "même", "et", "étais", "été", "était", "étaient", "étions", "étiez", "dans", "on", "alors", "parce", "que", "quoi", "pourquoi", "qui", "aviez", "sur", "donc", "peut", "maintenant", "sous", "il", "vous", "elle-même", "a", "juste", "ou", "aussi", "seulement", "moi-même", "lequel", "ceux", "après", "peu", "qui", "être", "si", "leur", "mon", "par", "faire", "il", "comment", "plus", "ici"}
dictionnaire_inutile = dictionnaire_inutile_en.union(dictionnaire_inutile_fr)

# Dictionnaire des mots abrégés
dictionnaire_jargon_fr = [("mrc", "merci"), ("bjr", "bonjour"), ("dr", "derien"), (
    "tlmt", "tellement"), ("jsp", "je sais pas"), ("cad", "c est à dire"), ("càd", "c est à dire")]

# Dictionnaire des insultes
dictionnaire_insultes_en = {"fuck", "shit", "bullshit", "bollocks", "crap", "damn", "goddamn", "dumb", "bastard", "scumbag", "cunt", "pussy", "twat", "ass", "arse", "asshole", "arsehole", "asshat",
                            "badass", "slut", "bitch", "skank", "whore", "hooker", "faggot", "piss", "dick", "dickhead", "cock", "turd", "jeck", "dumbass", "bugger", "wanker", "tosser", "tramp", "nigger", "nigga", "negro"}

with open(chemin + 'insult.txt', 'r') as fichier:
    dictionnaire_insultes_fr = set(fichier.read().splitlines())

dictionnaire_insulte = dictionnaire_insultes_en.union(dictionnaire_insultes_fr)

## FONCTIONS NETTOYAGE ##

# Enlever la ponctuation, les sauts de lignes, les caractères spéciaux


def nettoyage(txt):
    # On enlève les caractères spéciaux
    l = ""
    for j in txt:
        if (j.isalpha() or j.isspace()):
            l += j.lower()
        elif j == "'":
            l += ' '

    # On enlève les sauts de ligne
    b = l.replace('\n', '').split(' ')
    c = []
    for i in b:
        if i != "":
            c.append(i)
    d = ' '.join(c)

    return d


# Enlever les mots sémantiquement peu importants, je remplace le jargon


def nettoyage_semantique(txt):
    b = txt.split(' ')
    d = dictionnaire_inutile
    dj = dictionnaire_jargon_fr
    m = []
    n = ''
    for i in b:
        a = True
        for j in range(len(dj)):
            if i == dj[j][0]:
                n = dj[j][1]
                if i not in d:
                    a = False
                    m.append(n)
        if a == True:
            m.append(i)
    return m

# TextBlob : lemmatisation des mots (on radicalise)


def lemmatization(m):
    l = []

    for i in m:
        mot = TextBlob(i)
        # print(i)
        a = Word(mot)
        b = mot.tags[0][1]
        if b in ('NN', 'VBD', 'JJ', 'NNS', 'VBZ'):  # on lemmatize les verbes, noms, adjectifs
            # print(Word(mot).lemmatize(mot.tags[0][1]))
            l.append(Word(mot.words.singularize()[
                     0]).lemmatize(mot.tags[0][1]))
        else:
            l.append(i)

    # enlever les type txtBlob
    for i in range(len(l)):
        if type(l[i]) == type(TextBlob(Word('word'))):
            l[i] = l[i].tags[0][0]

    return l


# fonction pour globaliser l'appel des fonctions


def nettoyage_total(txt):
    return lemmatization(nettoyage_semantique(nettoyage(txt)))

## FONCTIONS DETECTEUR INSULTES V1 ##


def contains(small, big):  # renvoie si une liste appartient une autre (avec les mots consécutifs)
    for i in range(1 + len(big) - len(small)):
        if small == big[i:i+len(small)]:
            return True
    return False


def detecteur_v1(txt):  # renvoie si le texte est insultant ou non

    l = nettoyage_total(txt)
    b = False
    ins = []

    for i in dictionnaire_insulte:
        if len(i.split(' ')) <= len(l):
            if contains(i.split(' '), l):
                b = True
                ins.append(i)

    return b


if __name__ == "__main__":
    print(detecteur_v1(texte_en))
