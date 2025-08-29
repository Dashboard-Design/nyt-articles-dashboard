# import dash_bootstrap_components as dbc
# from dash import html

# def create_search_section():
#     return dbc.Container(
#     [
#         html.H4("Explore Article Trends", className="text-center"),
#         html.P(
#             "Search for keywords to analyze article publication trends over the last 15 years",
#             className="mt-2 text-center text-muted fs-6",
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.Input(
#                         type="text",
#                         placeholder="Enter keywords to analyze (e.g., climate change, technology, politics)",
#                     ),
#                     width=9,
#                 ),
#                 dbc.Col(
#                     dbc.Button("Analyze", color="secondary", className="w-100"),
#                     width=2,
#                 ),
#             ],
#             justify="center",
#             className="mt-3  fs-6",
#         ),
#     ],
#     className="my-5 bg-white p-4 rounded-3"
#     )

# import dash_bootstrap_components as dbc
# from dash import html

# def create_search_section():
#     return dbc.Container(
#     [
#         html.H4("Explore Article Trends", className="text-center"),
#         html.P(
#             "Search for keywords to analyze article publication trends over the last 15 years",
#             className="mt-2 text-center text-muted fs-6",
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.Input(
#                         id="keyword-input",
#                         type="text",
#                         placeholder="Enter keywords to analyze (e.g., climate change, technology, politics)",
#                     ),
#                     width=9,
#                 ),
#                 dbc.Col(
#                     dbc.Button(
#                         "Analyze", 
#                         id="search-button",
#                         color="secondary", 
#                         className="w-100"
#                     ),
#                     width=2,
#                 ),
#             ],
#             justify="center",
#             className="mt-3  fs-6",
#         ),
#     ],
#     className="shadow-sm my-5 bg-white p-4 rounded-3"
#     )


# search_section.py
import dash_bootstrap_components as dbc
from dash import html

def create_search_section():
    return dbc.Container([
        html.H1("Explore Article Trends", className="text-center mb-2", style={'fontWeight': '600', 'color': '#2D3748'}),
        html.P(
            "Search for keywords to analyze article publication trends over the last 10 years",
            className="text-center mb-4",
            style={'color': '#718096', 'fontSize': '16px'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(
                        id="keyword-input",
                        type="text",
                        placeholder="Enter keywords to analyze (e.g., climate change, technology, politics)",
                        className="py-2",
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
            className="w-100 g-1 justify-content-center",
        ),
    ], fluid=True, className="p-5 bg-white shadow-sm m-0", style={'borderRadius': '12px', 'maxWidth': '1300px'}
    )