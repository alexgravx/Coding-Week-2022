## Importation ##

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from projet_w2.InsultBlock.tweets_collect.to_dataframe import to_dataframe

dash.register_page(__name__, path="/subject",
                   title='Insultes par sujet', name='subject')


layout = html.Div(id="page-content", children=[])
