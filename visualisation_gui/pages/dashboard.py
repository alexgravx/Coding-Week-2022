## Importation ##

import dash
import nltk
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc, Input, Output, callback
from dash.dependencies import Input, Output
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe
from projet_w2.InsultBlock.insult_detector.main_detector import detecteur

dash.register_page(__name__, path='/dashboard', title='Accueil',
                   name='accueil', order=0,)


layout = html.Div([
    html.H6("Détecteur d'insultes"),
    html.Div([

        dcc.Input(id='my-input', value='insérer le texte', type='text')
    ]),
    html.Br(),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='my-output'),
    html.Div(id='output-state')

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value'),
    Input('submit-val', 'n_clicks')

)
def update_output_div(input_value, n_clicks):

    if n_clicks >= 1:
        n_clicks = 0
        if detecteur(input_value) == True:
            return f'{n_clicks}'+"c'est une insulte"
        else:
            return f'{n_clicks}'+"Ce n'est pas une insulte"

    return f'{n_clicks}'
