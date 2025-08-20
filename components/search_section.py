import dash_bootstrap_components as dbc
from dash import html

def create_search_section():
    return dbc.Container(
    [
        html.H4("Explore Article Trends", className="text-center"),
        html.P(
            "Search for keywords to analyze article publication trends over the last 15 years",
            className="mt-2 text-center text-muted fs-6",
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
                    dbc.Button("Analyze", color="secondary", className="w-100"),
                    width=2,
                ),
            ],
            justify="center",
            className="mt-3  fs-6",
        ),
    ],
    className="my-5 bg-white p-4 rounded-3"
    )