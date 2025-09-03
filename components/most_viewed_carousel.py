import dash_bootstrap_components as dbc
from dash import html
import pandas as pd

def create_most_viewed_carousel(df_most_viewed_l30):
    # Carousel items
    items = []
    for _, row in df_most_viewed_l30.iterrows():
       
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
            "img_style": {
                "height": "500px",
                "objectFit": "cover",
                "width": "100%",
                "background-color": "#f8f9fa"
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
        className="carousel-fade",
        # Style the carousel container
        style={
            "maxWidth": "900px",  # Control overall carousel width
            "margin": "0 auto"  # Center the carousel
        }
    )
    
    # Create the table of articles
    table_data = df_most_viewed_l30  
    
    table_rows = []
    for _, row in table_data.iterrows():
        # Truncate title if too long
        title = row['title']
        if len(title) > 60:
            title = title[:57] + "..."
            
        table_rows.append(
            html.Tr([
                html.Td([
                    html.A(
                        title,
                        href=row['web_url'],
                        target="_blank",
                        style={
                            "color": "#444444",
                            "textDecoration": "none",
                            "fontSize": "14px",
                            "fontWeight": "500"
                        }
                    )
                ]),
                html.Td(
                    row['section_name'] if pd.isna(row['subsection']) else f"{row['section_name']} - {row['subsection']}",
                    style={"fontSize": "13px", "color": "#718096"}
                ),
                html.Td([
                    html.A(
                        "Link 🧷",
                        href=row['web_url'],
                        target="_blank",
                        style={
                            "color": "#3182CE",
                            "textDecoration": "none",
                            "fontSize": "13px",
                            "fontWeight": "500"
                        }
                    )
                ], style={"textAlign": "right"})
            ])
        )
    
    # Create the table
    articles_table = dbc.Table(
        [
            html.Thead(html.Tr([
                html.Th("Article Title", style={"fontSize": "14px", "fontWeight": "600"}),
                html.Th("Section", style={"fontSize": "14px", "fontWeight": "600"}),
                html.Th("", style={"fontSize": "14px", "fontWeight": "600"})
            ])),
            html.Tbody(table_rows)
        ],
        bordered=False,
        striped=False,
        responsive=True,
        style={
            "width": "100%",
            "margin": "0"
        }
    )
    
    return html.Div([
        # Header with eye icon and title in one line
        html.Div([
            html.I(
                className="fas fa-eye me-3", 
                style={'color': '#155DFC', 'fontSize': '26px', 'verticalAlign': 'middle'}
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
        ], className="mb-4"),
        
        # Carousel and table in a row
        dbc.Row([
            dbc.Col(
                html.Div([
                    carousel
                ]),
                width=9
            ),
            
            dbc.Col(
                html.Div([
                    # html.H5(
                    #     "Top Articles",
                    #     className="mb-3",
                    #     style={'fontWeight': '600', 'color': '#2D3748'}
                    # ),
                    html.Div(
                        articles_table,
                        style={
                            "height": "500px",
                            "overflowY": "auto",
                            "border": "1px solid #e2e8f0",
                            "borderRadius": "8px",
                            "padding": "10px"
                        }
                    )
                ]),
                width=3
            )
        ], className="g-4"
        )  
    ],
    className="mt-3 mb-5"
)