## Importation ##

import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, State, callback
from dash.dependencies import Input, Output
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe
from projet_w2.InsultBlock.tweets_collect.main_collect import *
from projet_w2.InsultBlock.tweets_analysis.stats import ajout_colonnes, ajout_colonnes_2

## Code ##

dash.register_page(__name__, path="/subject",
                   title='Insultes par thème', name='subject')

dff = main_subject('politique')

fig = px.scatter(dff, x="user.followers_count", y="retweet_count",
                 size="favorite_count", color="user.verified")

layout = html.Div(
    children=[
        html.H1('Analyse des tweets par thème',
                style={'padding-left': '20px'}),
        dbc.Row([
            dbc.Col(dbc.Input(placeholder="Entrer un thème",
                              id='subject_name', type='text')), dbc.Col(dbc.Button('Submit', id='submit-val', n_clicks=0, style={'background': '#FF7C7C'}))], style={'width': '48%', 'padding': '10px 10px 10px 20px'}),
        dbc.Row([

            dbc.Col(
                dbc.Select(options=[{'value': 'favorite_count', 'label': 'Nombre de likes'}, {'value': 'retweet_count', 'label': 'Nombre de retweets'}, {'value': 'user.followers_count', 'label': 'Nombre de followers'},
                                    {'value': 'user.friends_count', 'label': "Nombre d'amis"}, {'value': 'insult', 'label': 'Caractère insultant du tweet'}, {'value': 'nb_insult_user', 'label': "Nombre d'insultes postées par l'utilisateur"}], id='menu_abcisses-user')),

            dbc.Col(
                dbc.Select(options=[{'value': 'favorite_count', 'label': 'Nombre de likes'}, {'value': 'retweet_count', 'label': 'Nombre de retweets'}, {'value': 'user.followers_count', 'label': 'Nombre de followers'},
                                    {'value': 'user.friends_count', 'label': "Nombre d'amis"}, {'value': 'insult', 'label': 'Caractère insultant du tweet'}, {'value': 'nb_insult_user', 'label': "Nombre d'insultes postées par l'utilisateur"}], id='menu_ordonnées-user'))
        ]),
        html.Div(
            dcc.Graph(id='dash_graph_user', style={'padding': '30px 0 0 0'}))
    ])


@ callback(
    Output('dash_graph', 'figure'),
    State('subject_name', 'value'),
    Input('submit-val', 'n_clicks'),
    Input('menu_abcisses', 'value'),
    Input('menu_ordonnées', 'value'))
def update_graphe(subject_name, n_clicks, xaxis_column_name, yaxis_column_name):
    if n_clicks >= 1:
        n_clicks = 0
        dff = main_subject(subject_name)
        dff = ajout_colonnes_2(ajout_colonnes(dff))
    fig = px.scatter(dff, x=xaxis_column_name,
                     y=yaxis_column_name)

    fig.update_xaxes(title=xaxis_column_name, type='linear')

    fig.update_yaxes(title=yaxis_column_name, type='linear')

    return fig


data_twitter = to_dataframe('data_missile.json')

fig = px.scatter(data_twitter, x="user.followers_count", y="favorite_count",
                 size="retweet_count", color="user.verified", size_max=50)
