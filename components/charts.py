import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objects as go
from dash import html

def create_metric_card(title, value, value_id, subtitle, icon, color="#3182CE"):
    """Create a metric card component matching the Figma design"""
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                # Icon
                html.Div(
                    html.I(className=f"{icon} me-2", style={'color': color, 'fontSize': '18px'}),
                    style={'display': 'inline-block', 'verticalAlign': 'middle'}
                ),
                # Value
                html.H4(
                    id=value_id,
                    children=value,
                    className="mb-1",
                    style={'fontWeight': '600', 'color': '#2D3748', 'display': 'inline-block', 'verticalAlign': 'middle'}
                ),
            ], className="mb-2"),
            html.P(title, className="mb-0", style={'color': '#718096', 'fontSize': '14px'}),
            html.P(subtitle, className="mb-0", style={'color': '#A0AEC0', 'fontSize': '12px'})
        ]),
        className="h-100 p-2 border-0 bg-white shadow-sm", style={'borderRadius': '12px'}
    )

def create_trend_chart_section():
    """Create the main chart section with cards"""
    # Create initial empty figure
    initial_fig = go.Figure()
    initial_fig.update_layout(
        title={
            'text': "Article Publication Trends",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#2D3748'}
        },
        xaxis_title="Year",
        yaxis_title="Number of Articles",
        # plot_bgcolor='white',
        # paper_bgcolor='white',
        font={'color': '#718096'},
        height=500,
        showlegend=False,
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='#E2E8F0'
        ),
        yaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='#E2E8F0'
        )
    )
        
    return dbc.Container([
        dbc.Row( [
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Article Publication Trends", className="mb-1 mt-2", style={'fontWeight': '600', 'color': '#2D3748'}),
                        html.P("Article publication frequency from 2015 to 2025", className="mb-2", style={'color': '#718096'}),
                        dcc.Graph(
                            id="trend-chart",
                            figure=initial_fig,
                            config={'displayModeBar': False},
                            style={'height': '500px'}
                        )
                    ] ,className="p-3"  )
                ],className="border-0")
            ], className="border-0 bg-white shadow-sm", style={'borderRadius': '12px'},
               width=9
            ),
            
            dbc.Col([
                dbc.Row([
                    dbc.Col(create_metric_card(
                        "Total Articles", 
                        "--", 
                        "total-articles-card",
                        "all articles",
                        "fas fa-newspaper"
                    ), width=12, className="h-100 mb-3"),
                    
                    dbc.Col(create_metric_card(
                        "Last Two Years", 
                        "--", 
                        "last-two-years-card",
                        "2023-2024",
                        "fas fa-chart-bar"
                    ), width=12, className="h-100 mb-3"),
                    
                    dbc.Col(create_metric_card(
                        "Growth vs Previous 2Y", 
                        "--", 
                        "growth-card",
                        "vs 2021-2022",
                        "fas fa-chart-line"
                    ), width=12, className="h-100 mb-3"),
                    
                    dbc.Col(create_metric_card(
                        "Avg/Month", 
                        "--", 
                        "avg-monthly-card",
                        "across all years",
                        "fas fa-calendar-alt"
                    ), width=12)
                ], className="g-3") 
            ], width=3
            )
        ],
            className="g-5"
        )
    ], fluid=True
    )

# fluid=True, className="p-5 bg-white shadow-sm", style={'borderRadius': '12px', 'maxWidth': '1500px'})