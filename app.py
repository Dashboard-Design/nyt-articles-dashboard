import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Custom Components
from components.navbar import create_navbar
from components.search_section import create_search_section
from components.data_load import load_data
from components.charts import create_trend_chart_section
from components.most_viewed_carousel import create_most_viewed_carousel
from components.line_chart import line_chart_generator
from components.footer import create_footer


df, df_most_viewed_l30, monthly_trends_all = load_data()

# Initialize app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
])


# App Layout
app.layout = html.Div(
    style={'backgroundColor': '#F7FAFC', 'minHeight': '100vh'},
    children=[
        dcc.Location(id="url", refresh=False),  # 👈 track the URL hash
        create_navbar(),

        html.Div([
            html.Div([
                html.Div(style={'height': '40px'}),

                html.Div(id="analysis", children=[
                    create_search_section()
                ]),
                
                html.Div(style={'height': '30px'}),
                create_trend_chart_section(),

                html.Div(style={'height': '40px'}),

                html.Div(id="most-viewed-section", children=[
                    create_most_viewed_carousel(df_most_viewed_l30)
                ]),

                html.Div(style={'height': '30px'})
            ])
        ], style={"maxWidth": "1300px", "margin": "0 auto"}),

        html.Div(id="footer-section", children=[create_footer()])
    ]
)

@app.callback(
    [
     Output('trend-title', 'children'),
     Output('trend-chart', 'figure'),
     Output('total-articles-card', 'children'),
     Output('last-two-years-card', 'children'),
     Output('growth-card', 'children'),
     Output('avg-monthly-card', 'children')],
    [Input('search-button', 'n_clicks')],
    [Input('keyword-input', 'value')]
)
def update_trend_analysis(n_clicks, keyword):
    # if no search has been performed yet
    if (not n_clicks) or (not keyword) or (keyword.strip() == ""):
        fig = line_chart_generator(monthly_trends_all)
        
        total_articles = len(df)
        
        # (2023 and 2024)
        last_two_years = len(df[df['year'].isin([2023, 2024])])
        
        # (2021 and 2022)
        previous_two_years = len(df[df['year'].isin([2021, 2022])])
        
        # Growth
        growth_pct = round(((last_two_years - previous_two_years) / previous_two_years) * 100, 1)
        growth_text = f"{'▲' if growth_pct > 0 else '▼'}{abs(growth_pct):.1f}%"
        
        # Average
        months_span = monthly_trends_all['year_month'].nunique()
        avg_monthly = round(total_articles / months_span, 1)
        
        return "Article Publication Trends", fig, f"{total_articles:,}", f"{last_two_years:,}", growth_text, f"{avg_monthly:,.1f}"

        
    keyword_lower = keyword.lower().strip()
    
    # Filter dataframe using search
    mask = df['search_text'].fillna('').astype(str).str.lower().str.contains(keyword_lower, case=False, na=False, regex=False)
    filtered_df = df[mask].copy()
    
    if len(filtered_df) == 0:
        fig = go.Figure()
        fig.update_layout(
            title=f"No articles found containing '{keyword}'",
            template="plotly_white",
            height=500
        )
        return fig, "0", "No Results", "No Data", "0"
    
    monthly_counts = filtered_df.groupby('year_month').size().reset_index(name='count')
    monthly_counts['date'] = monthly_counts['year_month'].dt.to_timestamp()
    
    fig = line_chart_generator(monthly_counts)
    
    total_articles = len(filtered_df)
    
    # (2023 and 2024)
    last_two_years = len(filtered_df[filtered_df['year'].isin([2023, 2024])])
    
    # (2021 and 2022)
    previous_two_years = len(filtered_df[filtered_df['year'].isin([2021, 2022])])
    
    # Growth 
    growth_pct = round(((last_two_years - previous_two_years) / previous_two_years) * 100, 1)
    growth_text = f"{growth_pct:+.1f}%"
    
    # Average 
    months_span = monthly_counts['year_month'].nunique()
    avg_monthly = round(total_articles / months_span, 1)
    
    return f"Article Publication Trends for '{keyword}'", fig, f"{total_articles:,}", f"{last_two_years:,}", growth_text, f"{avg_monthly:.1f}"
    
if __name__ == "__main__":
    app.run(debug=True)