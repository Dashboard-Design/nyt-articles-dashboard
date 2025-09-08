import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    return dbc.Navbar(
        dbc.Container([
            # Left side: Logo, brand, and update text, all grouped in one Row
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(src="/assets/icons8-statistics-96.png", height="26px"),
                        width="auto", # Allows the column to take up only the space it needs
                    ),
                    dbc.Col(
                        html.Div(
                            [
                                dbc.NavbarBrand(
                                    "NYTimes Analytics",
                                    className="ms-3 me-1", # Use margin-end (right) for spacing
                                    style={
                                        'fontWeight': '600',
                                        'color': '#2D3748',
                                        'fontSize': '1.25rem'
                                    }
                                ),
                                html.Span(
                                    "Updates every week",
                                    className="me-auto", # Pushes the text to the right within the column
                                    style={
                                        'fontWeight': '350',
                                        'color': "#718096",
                                        'fontSize': '0.875rem',
                                        'whiteSpace': 'nowrap',
                                        'marginLeft': '14px',
                                        'marginTop':'4px'
                                    }
                                ),
                            ],
                            className="d-flex align-items-center" # Use Flexbox to align items
                        ),
                        width="auto", # Ensures the column fits its content
                    ),
                ],
                align="center",
                className="g-0", # Removes gutter space between columns
            ),

            # Right side: Navigation links
            dbc.Nav(
                [
                    dbc.NavItem(
                        dbc.NavLink(
                            "Trend Analysis",
                            href="#analysis",
                            external_link=True,
                            className="nav-link-custom me-3", # Added margin to the right
                            style={
                                'color': '#2D3748',
                                'fontSize': '1rem',
                                'fontWeight': '420',
                                'padding': '8px 16px',
                                'borderRadius': '6px',
                                'transition': 'all 0.3s ease'
                            }
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "Most Viewed",
                            href="#most-viewed-section",
                            external_link=True,
                            className="nav-link-custom me-3", # Added margin to the right
                            style={
                                'color': '#2D3748',
                                'fontSize': '1rem',
                                'fontWeight': '420',
                                'padding': '8px 16px',
                                'borderRadius': '6px',
                                'transition': 'all 0.3s ease'
                            }
                        )
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            "About",
                            href="#footer-section",
                            external_link=True,
                            className="nav-link-custom",
                            style={
                                'color': '#2D3748',
                                'fontSize': '1rem',
                                'fontWeight': '420',
                                'padding': '8px 16px',
                                'borderRadius': '6px',
                                'transition': 'all 0.3s ease'
                            }
                        )
                    ),
                ],
                className="ms-auto", # Pushes the nav links to the right
                navbar=True,
            ),
        ],
        fluid=True,
        style={'maxWidth': '1300px', 'margin': '0 auto'}
        ),
        color="white",
        dark=False,
        sticky="top",
        className="shadow-sm",
        style={
            'width': '100%',
            'height': '60px',
            'fontFamily': "'Inter', 'Segoe UI', sans-serif"
        }
    )