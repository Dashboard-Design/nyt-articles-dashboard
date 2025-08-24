import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objects as go

def create_metric_card(title, value_id, icon_class, color="primary", initial_value="--"):
    """Create a metric card component"""
    return dbc.Card(
        dbc.CardBody([
            html.Div([
                html.I(className=f"{icon_class} fa-2x mb-2", style={'color': f'var(--bs-{color})'}),
                html.H4(id=value_id, children=initial_value, className="card-title mb-1"),
                html.P(title, className="card-text text-muted small mb-0")
            ], className="text-center")
        ]),
        className="h-100 w-100 shadow-sm"
    )

def create_trend_chart_section():
    """Create the main chart section with cards"""
    # Create initial empty figure
    initial_fig = go.Figure()
    initial_fig.update_layout(
        title="Enter a keyword and click 'Analyze' to see trends",
        xaxis_title="Year",
        yaxis_title="Number of Articles",
        template="plotly_white",
        height=450
    )
    
    return dbc.Container([
        dbc.Row([
            # Chart Column
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H6("Publication Trends Over Time", className="mb-0")),
                    dbc.CardBody([
                        dcc.Graph(
                            id="trend-chart",
                            figure=initial_fig,
                            config={'displayModeBar': False},
                            style={'height': '450px'}
                        )
                    ], className="p-1")
                ], className="shadow-sm h-100")
            ], width=9),
            
            # Cards Column
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        create_metric_card(
                            "Total Articles", 
                            "total-articles-card", 
                            "fas fa-newspaper",
                            "primary"
                        )
                    ], width=12, className="mb-3"),
                    
                    dbc.Col([
                        create_metric_card(
                            "Peak Year", 
                            "peak-year-card", 
                            "fas fa-chart-line",
                            "success"
                        )
                    ], width=12, className="mb-3"),
                    
                    dbc.Col([
                        create_metric_card(
                            "Recent Trend", 
                            "recent-trend-card", 
                            "fas fa-trending-up",
                            "info"
                        )
                    ], width=12, className="mb-3"),
                    
                    dbc.Col([
                        create_metric_card(
                            "Avg/Month", 
                            "avg-monthly-card", 
                            "fas fa-calendar-alt",
                            "warning"
                        )
                    ], width=12)
                ])
            ], width=3)
        ], className="g-4 w-100")
    ], className = "w-100")