import pandas as pd
import plotly.graph_objects as go

# Read the Excel sheet
df = pd.read_excel("Heat_map.csv.xlsx")

# Define color mapping
color_mapping = {
    "Dark Green": "#006400",
    "One Level Below Dark Green": "#228B22",
    "Two-Level Below Dark Green": "#32CD32",
    "Two-Level Above Light Green": "#FFD700",
    "One Level Above Light Green": "#ADFF2F",
    "Light Green": "#00FF00",
    "White": "#FFFFFF",
    "Two Level Above Light Green": "#ADFF2F",
    "Two Level Below Dark Green": "#32CD32"
}

# Create the heatmap figure
fig = go.Figure(data=go.Treemap(
    labels=df['Area'],
    parents=[''] * len(df['Area']),
    values=df['Existing team members proficient with this area'],
    text=df['Average team expertise(1-5)'],
    hovertemplate='<b>%{label}</b><br>Size: %{value}<br>Expertise: %{text}',
    marker=dict(
        colors=[color_mapping[level] for level in df['Average team expertise(1-5)']],
        line=dict(width=2, color='white')
    )
))

# Update layout
fig.update_layout(
    title="Team Expertise Heatmap",
    margin=dict(t=0, l=0, r=0, b=0)
)

# Show the figure
fig.show()
