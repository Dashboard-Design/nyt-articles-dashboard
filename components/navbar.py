import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    return dbc.Navbar(
        dbc.Container([
            # Left side: Logo and brand
            dbc.Row([
                dbc.Col(html.Img(src="/assets/icons8-statistics-96.png", height="26px")),
                dbc.Col(dbc.NavbarBrand(
                    "NYTimes Analytics", 
                    className="ms-3",
                    style={
                        'fontWeight': '600', 
                        'color': '#2D3748',
                        'fontSize': '20px'
                    }
                )),
            ], align="center", className="g-0"),
            
            # Center: Update text (now in a single line)
            html.Div(
                "Updates every week",
                style={
                    'fontWeight': '300', 
                    'color': "#718096",
                    'fontSize': '14px',
                    'whiteSpace': 'nowrap',
                    'position': 'absolute',
                    'left': '50%',
                    'transform': 'translateX(-50%)'
                }
            ),
            
            # Right side: Navigation links
            dbc.Nav([
                dbc.NavItem(dbc.NavLink(
                    "Trend Analysis", 
                    href="#analysis", 
                    external_link=True,
                    className="nav-link-custom",
                    style={
                        'color': '#2D3748', 
                        'fontWeight': '450', 
                        'marginRight': '25px',
                        'padding': '8px 16px',
                        'borderRadius': '6px',
                        'transition': 'all 0.3s ease'
                    }
                )),
                dbc.NavItem(dbc.NavLink(
                    "Most Viewed", 
                    href="#most-viewed-section", 
                    external_link=True,
                    className="nav-link-custom",
                    style={
                        'color': '#2D3748', 
                        'fontWeight': '450', 
                        'marginRight': '25px',
                        'padding': '8px 16px',
                        'borderRadius': '6px',
                        'transition': 'all 0.3s ease'
                    }
                )),
                dbc.NavItem(dbc.NavLink(
                    "About", 
                    href="#footer-section", 
                    external_link=True,
                    className="nav-link-custom",
                    style={
                        'color': '#2D3748', 
                        'fontWeight': '450',
                        'padding': '8px 16px',
                        'borderRadius': '6px',
                        'transition': 'all 0.3s ease'
                    }
                )),
            ], className="ms-auto", navbar=True),
        ], fluid=True, style={'position': 'relative', 'maxWidth': '1300px', 'margin': '0 auto'}),
        color="white",
        dark=False,
        sticky="top",
        className="shadow-sm",
        style={
            'padding': '12px 0', 
            'height': '60px',
            'fontFamily': "'Inter', 'Segoe UI', sans-serif"
        }
    )