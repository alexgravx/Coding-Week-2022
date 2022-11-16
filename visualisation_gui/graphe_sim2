from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

from projet_w2.InsultBlock.tweets_collect.main_collect import *

df = main_subject('grève', 200)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider', figure={}),
    dcc.Slider(0, 1, step=None, marks={
               0: 'Certifié', 1: 'non certifié'}, id='verified_slider')
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('verified_slider', 'value'))
def update_figure(state):
    filtered_df = df[df.users_verified == state]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
