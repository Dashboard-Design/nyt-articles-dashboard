import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    return dbc.Navbar(
        dbc.Container([
            dbc.Row([
                dbc.Col(html.Img(src="/assets/icons8-statistics-96.png", height="26px")),
                dbc.Col(dbc.NavbarBrand("NYTimes Analytics", className="ms-3", style={'fontWeight': '600', 'color': '#2D3748'})),
            ],
            align="center",
            className="g-0",
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Updates", href="#", style={
                    'backgroundColor': '#3182CE', 
                    'color': 'white', 
                    'borderRadius': '6px',
                    'padding': '8px 16px',
                    'fontWeight': '500'
                })),
            ],
            className="ms-auto",
            navbar=True,
            ),
        ]),
        color="white",
        dark=False,
        sticky="top",
        className="shadow-sm",
        style={'padding': '10px 0'}
    )