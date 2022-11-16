## Importation ##

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
from projet_w2.InsultBlock.visualisation_gui.app import fig, fig1

df = pd.read_csv(
    'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("InsultBlock", className="display-4"),
        html.Hr(),
        html.P(
            "Recherche par", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/dashboard", active="exact"),
                dbc.NavLink("Subject", href="/subject", active="exact"),
                dbc.NavLink("User", href="/user", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/dashboard":
        return [
            html.H1('Insulte par Dashboard',
                    style={'textAlign': 'center'}),

        ]
    elif pathname == "/subject":
        return [
            html.H1('Insulte par thème',
                    style={'textAlign': 'center'}),

        ]
    elif pathname == "/user":
        return [
            html.H1('Insulte par utilisateur',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='life-exp-vs-gdp', figure=fig1)

        ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)

## User ##
## Dash Board ##
## Thème ##
