## Importation ##

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe

## Code ##

dash.register_page(__name__, path="/subject",
                   title='Insultes par sujet', name='subject')

data_twitter = to_dataframe('data_missile.json')

fig = px.scatter(data_twitter, x="user.followers_count", y="favorite_count",
                 size="retweet_count", color="user.verified", size_max=50)

app.layout = html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
    print("ok")
