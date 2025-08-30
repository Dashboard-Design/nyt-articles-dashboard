import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

def create_most_viewed_carousel(df_most_viewed_l30):
    # Create the carousel items
    items = []
    for _, row in df_most_viewed_l30.iterrows():
        # Use a placeholder image if no image is available
        image_src = row.get('image', '/assets/article-placeholder.jpg')
        if pd.isna(image_src) or image_src == '':
            image_src = '/assets/article-placeholder.jpg'
            
        item = {
            "key": f"{row['id']}",
            "src": image_src,
            "header": f"{row['title']}",
            "caption": f"{str(row['keyword_one'])} - {str(row['keyword_two'])} - {str(row['keyword_three'])} - {str(row['keyword_four'])}",
            "href": f"{row['web_url']}",
            "external_link_target": "_blank",  # Open in new tab
            # Add image styling to control size and appearance
            "img_style": {
                "height": "500px",  # Control the height
                "objectFit": "cover",  # Ensures image covers the area without distortion
                "width": "100%",  # Full width of container
                "background-color": "#f8f9fa"  # Fallback background color
            }
        }
        items.append(item)
    
    # Create the carousel
    carousel = dbc.Carousel(
        items=items,
        controls=True,
        indicators=True,
        interval=5000,  # mili seconds
        ride="carousel",
        # Style the carousel container
        style={
            "maxWidth": "900px",  # Control overall carousel width
            "margin": "0 auto"  # Center the carousel
        }
    )
    
    return html.Div([
        # Header with eye icon and title in one line
        html.Div([
            html.I(
                className="fas fa-eye me-2", 
                style={'color': '#3182CE', 'fontSize': '28px', 'verticalAlign': 'middle'}
            ),
            html.H4(
                "Most Viewed Articles - Last 30 Days", 
                style={
                    'fontWeight': '600', 
                    'color': '#2D3748',
                    'display': 'inline-block',
                    'verticalAlign': 'middle',
                    'margin': '0'
                }
            )
        ], className="mb-5 mt-4"
        
        ),
        carousel
    ],
    className="mb-5"
    )