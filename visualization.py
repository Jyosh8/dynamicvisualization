import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pptx import Presentation
from pptx.util import Inches
import plotly.io as pio

def prepare_visualization(data):
    """Prepare data visualization using Plotly."""
    if data is None or data.empty:
        return None

    # Table with classification types and ATR Submitted and Mitigation Plan counts
    classification_types = ['High', 'Substantial', 'Moderate']
    classification_counts = {classification: (data['Classification'] == classification).sum() for classification in classification_types}

    # Create the table with counts of classifications and ATR/Mitigation plan status
    # Group by 'Work Name' and aggregate counts
    grouped_data = data.groupby('Work Name').agg(
        Date_of_Assessment=('Date of Assessment', 'first'),
        Risk_Status=('Status', 'first'),
        High_Count=('Classification', lambda x: (x == 'High').sum()),
        Substantial_Count=('Classification', lambda x: (x == 'Substantial').sum()),
        Moderate_Count=('Classification', lambda x: (x == 'Moderate').sum()),
        ATR_Submitted_Count=('ATR Date', lambda x: x.notna().sum()),
        Mitigation_Planned_Count=('Mitigation Plan', lambda x: x.notna().sum())
    ).reset_index()

    # Create the table
    table_fig = go.Figure(data=[go.Table(
        header=dict(
            values=[
                "Work Name", "Date of Assessment", "Risk Status",
                "High", "Substantial", "Moderate",
                "ATR Submitted", "Mitigation Planned"
            ],
            fill_color='lightblue',
            align='center',
            font=dict(color='black')
            
        ),
        cells=dict(
            values=[
                grouped_data['Work Name'],
                grouped_data['Date_of_Assessment'],
                grouped_data['Risk_Status'],
                grouped_data['High_Count'],
                grouped_data['Substantial_Count'],
                grouped_data['Moderate_Count'],
                grouped_data['ATR_Submitted_Count'],
                grouped_data['Mitigation_Planned_Count']
            ],
            fill_color='white',
            align='left',
            height=40  # Increase row height to accommodate wrapped text
        )
    )])

    table_fig.update_layout(
    title=dict(
        text="<b>Risk Assessment Table</b>",
        y=0.95,  # Adjust the vertical position of the title
        x=0.5,
        xanchor='center',
        yanchor='top',
        font=dict(size=16, color='black', family='Arial', weight='bold')
    ),
    margin=dict(t=80)  # Adjust the top margin to add space between the title and the table
    )
    
    
    # 2. Work vs Risk status (Bar chart)
    work_status_counts = data.groupby(['Work Name', 'Status']).size().unstack(fill_value=0)
    bar_fig = go.Figure()
    
    for status in work_status_counts.columns:
        bar_fig.add_trace(go.Bar(
            x=work_status_counts.index,
            y=work_status_counts[status],
            name=status
        ))

    bar_fig.update_layout(
        
        xaxis_title="Work Name",
        yaxis_title="Count of Risks",
        barmode='group',
        height=400
    )

    bar_fig.update_layout(
    title=dict(
        text="<b>Work vs Risk Status</b>",
        y=0.5,  # Adjust the vertical position of the title
        x=0.5,
        xanchor='center',
        yanchor='top',
        font=dict(size=16, color='black', family='Arial', weight='bold')
    ),
    margin=dict(t=80)  # Adjust the top margin to add space between the title and the table
    )
    
    # 3. Pie chart for Work Name vs Count of Risks
    work_name_counts = data['Work Name'].value_counts()
    pie_fig = go.Figure(data=[go.Pie(
        labels=work_name_counts.index,
        values=work_name_counts.values,
        hole=0.3
    )])

    pie_fig.update_layout(
       
        height=400,
        width=400,
        margin=dict(l=10, r=10, t=40, b=10),
        paper_bgcolor="white",
        plot_bgcolor="white",
        shapes=[
            dict(
                type="rect",
                xref="paper",
                yref="paper",
                x0=0,
                y0=0,
                x1=1,
                y1=1,
                line=dict(color="black", width=2)
            )
        ]
    )

    pie_fig.update_layout(
    title=dict(
        text="<b>Work Name vs Count of Risks</b>",
        y=0.95,  # Adjust the vertical position of the title
        x=0.5,
        xanchor='center',
        yanchor='top',
        font=dict(size=16, color='black', family='Arial', weight='bold')
    ),
    margin=dict(t=80)  # Adjust the top margin to add space between the title and the table
    )
    
    
    # Combine bar and pie charts side by side
    combined_fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.6, 0.4],
        specs=[[{"type": "bar"}, {"type": "pie"}]],
        subplot_titles=("Work vs Risk Status", "Work Name vs Count of Risks")
        
    )

    
    # Update layout to style titles and add space
    combined_fig.update_layout(
        title_text="<b>Combined Bar and Pie Charts</b>",
        title_x=0.5,
        title_y=0.95,
        title_xanchor='center',
        title_yanchor='top',
        title_font=dict(size=16, color='black', family='Arial', weight='bold'),
        margin=dict(t=100),  # Adjust the top margin to add space between the title and the charts
        showlegend=True
    )

        # Update layout to style titles and add space
    combined_fig.update_layout(
        annotations=[
            dict(
                text="<b>Work vs Risk Status</b>",
                x=0.27,
                y=1.05,

                showarrow=False,
                font=dict(size=14, color='black', family='Arial', weight='bold')
            ),
            dict(
                text="<b>Work Name vs Count of Risks</b>",
                x=0.8,
                y=1.05,

                showarrow=False,
                font=dict(size=14, color='black', family='Arial', weight='bold')
            )
        ])

    for trace in bar_fig.data:
        combined_fig.add_trace(trace, row=1, col=1)

    for trace in pie_fig.data:
        combined_fig.add_trace(trace, row=1, col=2)

 
    # Return all figures
    return table_fig, combined_fig
