import dash
from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc

# Custom Components
from components.navbar import create_navbar
from components.search_section import create_search_section

# Initialize app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout
app.layout = html.Div( 
    style={'backgroundColor': '#F9FAFB', 'minHeight': '100vh', 'padding': '0'},
    children = [create_navbar(), create_search_section()]
)

if __name__ == "__main__":
    app.run(debug=True)