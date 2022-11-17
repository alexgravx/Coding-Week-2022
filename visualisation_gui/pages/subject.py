## Importation ##

import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe

## Code ##

dash.register_page(__name__, path="/subject",
                   title='Insultes par sujet', name='subject')

data_twitter = to_dataframe('data_missile.json')

fig = px.scatter(data_twitter, x="user.followers_count", y="favorite_count",
                 size="retweet_count", color="user.verified", size_max=50)

layout = html.Div([html.H1('Insulte par thème',
                           style={'textAlign': 'center'}),
                   dcc.Graph(figure=fig),

                   ])
