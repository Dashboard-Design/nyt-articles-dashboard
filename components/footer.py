import dash_bootstrap_components as dbc
from dash import html

def create_footer():
    return html.Footer(
        dbc.Container([
            html.Hr( className="mb-4" ),
            dbc.Row([
                dbc.Col([
                    html.P("📖 About this project", className="fw-bold mb-2", style={'color': '#2D3748'}),
                    html.P(
                        "This dashboard was built to explore New York Times article trends "
                        "and highlight how data can reveal shifts in media focus. "
                        "I started this project to sharpen my data storytelling and web analytics skills. "
                        "In the future, I plan to expand the analysis and integrate new features.",
                        style={'color': '#4A5568', 'fontSize': '14px', 'padding-right': '50px'}
                    ),
                ], md=9),

                dbc.Col([
                    html.P("🔗 Connect with me", className="fw-bold mb-2", style={'color': '#2D3748'}),
                    dbc.Row([
                        html.A("LinkedIn: Sajjad Ahmadi",
                            href="https://www.linkedin.com/in/sajjadahmadi/",
                            target="_blank",
                            style={'color': '#3182CE', 'textDecoration': 'none', 'fontSize': '14px'}),
                        html.A("GitHub: Dashboard-Design",
                            href="https://github.com/Dashboard-Design",
                            target="_blank",
                            style={'color': '#3182CE', 'textDecoration': 'none', 'fontSize': '14px'})
                    ] , className="g-1" )           
                ], className="pl-2", md=3),
            ], className="g-3", align="start"),
            html.Div("© 2025 Sajjad Ahmadi – Built with Dash & Plotly",
                     style={'color': '#A0AEC0', 'fontSize': '12px', 'marginTop': '20px'})
        ], className="pt-4 pb-4"),
        style={'backgroundColor': '#F7FAFC', 'marginTop': '20'}
    )
