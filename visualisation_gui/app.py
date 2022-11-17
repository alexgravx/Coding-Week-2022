from textblob import TextBlob
import matplotlib.pyplot as plt
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from projet_w2.InsultBlock.tweets_collect.to_dataframe import *
from projet_w2.InsultBlock.insult_detector.main_detector import detecteur
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Fonction qui détermine la polarité d'un twwet
data = to_dataframe('data_EmmanuelMacron_agriculture.json')


def pol(twindex):
    tweet = TextBlob(data['text'][twindex])
    stm = tweet.sentiment[0]
    return stm

# Fonction qui count le nombre de retweet :


def nb_rtw(twindex):
    rt = data['retweet_count'][twindex]
    return rt

# Fonction qui count le nombre d'insultes par systèmes d'exploitations


def nb_insultes_par_sysex(sysex):
    n = 0
    for twindex in range(len(data.index)):
        if data['source'][twindex].split(' ')[-1] == sysex:
            texte = data['text'][twindex]
            L = detecteur(texte)
            # print(L)
            i = 0
            lis = lis_sysex()
            for j in range(len(lis)):
                if sysex == lis[j][0]:
                    i = j
            n += len(L)/lis[1][i]
    return n

# Fonction qui liste les systèmes d'exploitations utilisés dans le dataset


def lis_sysex():
    l = []
    for twindex in range(len(data.index)):
        l_sysex = [l[j][0] for j in range(len(l))]
        if data['source'][twindex].split(' ')[-1] not in l_sysex:
            l.append((data['source'][twindex].split(' ')[-1], 1))
        else:
            for j in range(len(l)):
                if data['source'][twindex].split(' ')[-1] == l[j][0]:
                    # print(l[j][1])
                    c = l[j][1] + 1
                    l[j] = (l[j][0], c)

    l_sysex = [l[j][0] for j in range(len(l))]
    l_nbtwi = [l[j][1] for j in range(len(l))]

    return (l_sysex, l_nbtwi)


print(lis_sysex())


X = [pol(i) for i in range(len(data.index))]
Y = [nb_rtw(i) for i in range(len(data.index))]
X1 = lis_sysex()[0]
Y1 = [nb_insultes_par_sysex(i) for i in X1]

print(Y1)

# Création du Data
df = pd.DataFrame({"systeme d'utilisation": X1,
                  "nombre d'insultes (en ratio aux nb de tweet sur le système)": Y1, })
# "user.followers_count": data['user.followers_count']})

fig = px.bar(df, x="systeme d'utilisation",
             y="nombre d'insultes (en ratio aux nb de tweet sur le système)")

if __name__ == '__main__':
    app.run_server(debug=True)

#df1 = data

# fig1 = px.scatter(df1, x="id", y="retweet_count",
    # size="retweet_count", hover_name="user.followers_count",
    # log_x=True, size_max=60)


# if __name__ == '__main__':
 #   app.run_server(debug=True)
