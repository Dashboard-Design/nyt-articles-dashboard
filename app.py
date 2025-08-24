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

# Load data once (cached)
df, df_most_viewed_l30 = load_data()
print("DataFrame columns:", df.columns.tolist())  # Debug line
print("DataFrame shape:", df.shape)  # Debug line

# Initialize app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
])

# App Layout
app.layout = html.Div( 
    style={'backgroundColor': '#F9FAFB', 'minHeight': '100vh', 'padding': '0'},
    children = [
        create_navbar(), 
        create_search_section(),
        create_trend_chart_section()
    ]
)

@app.callback(
    [Output('trend-chart', 'figure'),
     Output('total-articles-card', 'children'),
     Output('peak-year-card', 'children'),
     Output('recent-trend-card', 'children'),
     Output('avg-monthly-card', 'children')],
    [Input('search-button', 'n_clicks')],
    [Input('keyword-input', 'value')]
)
def update_trend_analysis(n_clicks, keyword):
    # Show placeholder chart if no search has been performed yet
    if (not n_clicks) or (not keyword) or (keyword.strip() == ""):
        fig = go.Figure()
        fig.update_layout(
            title="Enter a keyword and click 'Analyze' to see trends",
            xaxis_title="Year",
            yaxis_title="Number of Articles",
            template="plotly_white",
            height=450
        )
        return fig, "--", "--", "--", "--"
        
    keyword_lower = keyword.lower().strip()
    
    # Filter dataframe using simple contains search
    mask = df['search_text'].fillna('').astype(str).str.lower().str.contains(keyword_lower, case=False, na=False, regex=False)
    filtered_df = df[mask].copy()
    
    if len(filtered_df) == 0:
        fig = go.Figure()
        fig.update_layout(
            title=f"No articles found containing '{keyword}'",
            xaxis_title="Year",
            yaxis_title="Number of Articles",
            template="plotly_white",
            height=450
        )
        return fig, "0", "No Results", "No Data", "0"
    
    # Convert pub_date to datetime if it's not already

    filtered_df['published_date'] = pd.to_datetime(filtered_df['published_date'], errors='coerce')
    filtered_df = filtered_df.dropna(subset=['published_date'])
    
    # Extract year
    filtered_df['year'] = filtered_df['published_date'].dt.year
    
    # Group by year and count articles
    yearly_counts = filtered_df.groupby('year').size().reset_index(name='count')
    
    # Create line chart
    fig = px.line(
        yearly_counts, 
        x='year', 
        y='count',
        title=f"Article Publication Trends for '{keyword}'",
        labels={'count': 'Number of Articles', 'year': 'Year'}
    )
    
    fig.update_traces(
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=6)
    )
    
    fig.update_layout(
        template="plotly_white",
        hovermode='x unified',
        title_x=0.5,
        height=450,
        title=f"Articles containing '{keyword}' over time"
    )
    
    # Calculate card values
    total_articles = len(filtered_df)
    peak_year = yearly_counts.loc[yearly_counts['count'].idxmax(), 'year'] if not yearly_counts.empty else "N/A"
    
    # Recent trend (last 2 years vs previous 2 years)
    current_year = datetime.now().year
    recent_count = len(filtered_df[filtered_df['year'].isin([current_year-1, current_year-2])])
    previous_count = len(filtered_df[filtered_df['year'].isin([current_year-3, current_year-4])])
    
    if previous_count > 0:
        trend_pct = round(((recent_count - previous_count) / previous_count) * 100, 1)
        recent_trend = f"{trend_pct:+.1f}%"
    else:
        recent_trend = "N/A"
    
    # Average monthly (approximate)
    years_span = yearly_counts['year'].max() - yearly_counts['year'].min() + 1 if not yearly_counts.empty else 1
    avg_monthly = round(total_articles / (years_span * 12), 1)
    
    return fig, f"{total_articles:,}", str(peak_year), recent_trend, f"{avg_monthly:.1f}"
    


if __name__ == "__main__":
    app.run(debug=True)