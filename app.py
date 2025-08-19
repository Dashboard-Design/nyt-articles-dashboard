import dash
from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc

# Initialize app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Header + Navigation
navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png", height="20px")),
                    dbc.Col(dbc.NavbarBrand("NYTimes Analytics", className="ms-2")),
                ],
                align="center",
                className="g-0",
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Live Dashboard", href="#", className="btn btn-primary")),
                ],
                className="ms-auto",
                navbar=True,
            ),
        ]
    ),
    color="light",
    dark=False,
    sticky="top",
)

# Search section
search_section = dbc.Container(
    [
        html.H1("Explore Article Trends", className="text-center mt-5"),
        html.P(
            "Search for keywords to analyze article publication trends over the last 15 years",
            className="mt-3 text-center text-muted",
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(
                        type="text",
                        placeholder="Enter keywords to analyze (e.g., climate change, technology, politics)",
                    ),
                    width=9,
                ),
                dbc.Col(
                    dbc.Button("Analyze", color="primary", className="w-100"),
                    width=2,
                ),
            ],
            justify="center",
            className="mt-4",
        ),
    ],
    className="my-5",
)

# App Layout
app.layout = html.Div([navbar, search_section])

if __name__ == "__main__":
    app.run(debug=True)