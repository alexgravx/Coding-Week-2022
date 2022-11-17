## Importation ##

import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc, callback, Input, Output
from dash.dependencies import Input, Output
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe

from dash import html, Dash, dcc, Input, Output, State
import plotly.express as px
import pandas as pd

from projet_w2.InsultBlock.tweets_collect.main_collect import *

dash.register_page(__name__, path="/users",
                   title='Insultes par utilisateur', name='users')

df = main_user('sandrousseau')

fig = px.scatter(df, x="user.followers_count", y="retweet_count",
                 size="favorite_count", color="user.verified")

layout = html.Div(
    children=[
        html.H1(children='Sélectionner un utilisateur'),
        html.Div(dcc.Input(placeholder="Entrer nom d'utilisateur",
                           id='user_name', type='text')),
        html.Div([

            html.Div(
                 dcc.Dropdown(options={'favorite_count': 'Nombre de likes', 'retweet_count': 'Nombre de retweets', 'user.favourites_count': 'Nombre de Likes du compte', 'user.followers_count': 'Nombre de followers',
                                       'user.friends_count': "Nombre d'amis", 'insult': 'Caractère insultant du tweet', 'nb_insult_user': "Nombre d'insultes postées par l'utilisateur", 'os': "Système d'exploitation"}, id='menu_abcisses')),

            html.Div(
                dcc.Dropdown(options={'favorite_count': 'Nombre de likes', 'retweet_count': 'Nombre de retweets', 'user.favourites_count': 'Nombre de Likes du compte', 'user.followers_count': 'Nombre de followers',
                                      'user.friends_count': "Nombre d'amis", 'insult': 'Caractère insultant du tweet', 'nb_insult_user': "Nombre d'insultes postées par l'utilisateur", 'os': "Système d'exploitation"}, id='menu_ordonnées'))
        ]),
        html.Div(
            dcc.Graph(id='dash_graph'))
    ])


@callback(
    Output('dash_graph', 'figure'),
    Input('user_name', 'value'),
    Input('menu_abcisses', 'value'),
    Input('menu_ordonnées', 'value'))
def update_graphe(user_name, xaxis_column_name, yaxis_column_name):
    dff = main_user(user_name)
    fig = px.scatter(dff, x=xaxis_column_name,
                     y=yaxis_column_name)

    fig.update_xaxes(title=xaxis_column_name, type='linear')

    fig.update_yaxes(title=yaxis_column_name, type='linear')

    return fig
