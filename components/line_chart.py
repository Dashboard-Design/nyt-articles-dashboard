import plotly.express as px

def line_chart_generator(data_frame):
    """_summary_

    Args:
        data_frame (_type_): a pandas data frame

    Returns:
        _type_: figure
    """
    fig = px.line(
                data_frame, 
                x='date', 
                y='count',
                labels={'count': 'Number of Articles', 'date': 'Year-Month'}
    )
    fig.update_traces(
        mode="lines+markers",
        line=dict(color="#C9CBCE", width=2.5),
        marker=dict(size=6.5, color="#155DFC", symbol="circle")  
    )
    
    # Customize the layout for better aesthetics
    fig.update_layout(
        margin=dict(l=30, r=10, t=20, b=35), 
        title= None,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2D3748'),
        height=500,
        hovermode='x unified',
        showlegend=False,
        xaxis=dict(
            title = None,
            tickformat='%b %Y',
            tickmode='auto',
            nticks=12,  # Show approximately 12 ticks
            showgrid=True,
            gridcolor="#F5F5F5",
            gridwidth=0.4,
            zeroline=False,
            showline=True,
            linecolor='#C0C0C0',
            linewidth=0.4
        ),
        yaxis=dict(
            #title='Number of Articles',
            title = None,
            showgrid=True,
            gridcolor='#F5F5F5',
            gridwidth=0.4,
            zeroline=False,
            showline=True,
            linecolor="#C0C0C0",
            linewidth=0.4
        )
    )

    return fig


