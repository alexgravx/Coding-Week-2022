from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

from projet_w2.InsultBlock.tweets_collect.main_collect import *

df = main_subject('grève', 200)

app = Dash(__name__)


app.layout = html.Div([
    html.Div([

        html.Div(
            dcc.Dropdown(['favorite_count', 'retweet_count', 'user.created_at', 'user.favourites_count', 'user.followers_count',
                          'user.friends_count'], id='menu_abcisses')),

        html.Div(
            dcc.Dropdown(['favorite_count', 'retweet_count', 'user.created_at', 'user.favourites_count', 'user.followers_count',
                          'user.friends_count'], id='menu_ordonnées'))
    ]),

    html.Div(
        dcc.Graph(id='graphe_x_fonction_y'))
])


@app.callback(Output('graphe_x_fonction_y', 'figure'), Input('menu_abcisses', 'value'), Input('menu_ordonnées', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name):

    fig = px.scatter(df, x=xaxis_column_name,
                     y=yaxis_column_name)

    fig.update_xaxes(title=xaxis_column_name, type='linear')

    fig.update_yaxes(title=yaxis_column_name, type='linear')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
