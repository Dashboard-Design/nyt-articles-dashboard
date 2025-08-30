import dash_bootstrap_components as dbc
from dash import html

def create_search_section():
    return dbc.Container([
        html.H1("Explore Article Trends", className="text-center mb-2", style={'fontWeight': '600', 'color': '#2D3748'}),
        html.P(
            "Search for keywords to analyze article publication trends over the last 10 years",
            className="text-center mb-3",
            style={'color': '#718096', 'fontSize': '16px'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(
                        id="keyword-input",
                        type="text",
                        placeholder="Enter keywords to analyze (e.g., climate change, technology, politics)",
                        className="w-100 py-2",
                        style={'borderRadius': '8px', 'border': '1px solid #E2E8F0'}
                    ),
                    width=10,
                ),
                dbc.Col(
                    dbc.Button(
                        "Analyze", 
                        id="search-button",
                        color="primary", 
                        className="w-100 py-2",
                        style={'backgroundColor': '#3182CE', 'borderRadius': '8px', 'fontWeight': '600'}
                    ),
                    width=2,
                ),
            ],
            className="g-2 justify-content-center", style= {"maxWidth": "1000px", "margin": "0 auto"}
        ),
    ],fluid=True, className="p-5 bg-white shadow-sm justify-content-center", style={'borderRadius': '12px'}
    )
