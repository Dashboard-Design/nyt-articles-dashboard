import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    return dbc.Navbar(
    dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/icons8-statistics-96.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("NYTimes Analytics", className="ms-3")),
                    ],
                    align="center",
                    className="g-0",
                ),
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Live Dashboard", href="#", className="btn btn-info")),
                    ],
                    className="ms-auto",
                    navbar=True,
                ),
            ]
        ),
    color="white",
    dark=False,
    sticky="top",
)