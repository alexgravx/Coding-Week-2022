from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import matplotlib as plt

from projet_w2.InsultBlock.tweets_collect.main_collect import *

data_twitter = main_user('sandrousseau', 200)

app = Dash(__name__)


fig = px.scatter(data_twitter, x="user.followers_count", y="retweet_count",
                 size="favorite_count", color="user.verified", size_max=60)

app.layout = html.Div([dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run_server(debug=True)
