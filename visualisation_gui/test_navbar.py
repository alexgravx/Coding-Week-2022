"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.
Requires dash-bootstrap-components 0.3.0 or later
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import base64

Logo_src = "./projet_w2/InsultBlock/visualisation_gui/Logo.png"

encoded_image = base64.b64encode(open(Logo_src, 'rb').read())


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])


nav_item1 = dbc.NavItem(dbc.NavLink("Dashboard", href="#"))
nav_item2 = dbc.NavItem(dbc.NavLink("Subject", href="#"))
nav_item3 = dbc.NavItem(dbc.NavLink("Users", href="#"))


navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), height="30px")),
                        dbc.Col(dbc.NavbarBrand(
                            "InsultBlock", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://twitter.com/home",
                style={"textDecoration": "none"},
            ),
            dbc.Nav(
                [nav_item1, nav_item2, nav_item3],
                className="ms-auto",
                navbar=True,
            )
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

app.layout = html.Div([navbar])


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
