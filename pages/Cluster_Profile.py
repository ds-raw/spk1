# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:53:52 2024

@author: daffa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:50:06 2024

@author: daffa
"""
# Import necessary packages
from dash import html, register_page, dcc, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

register_page(
    __name__,
    name='Cluster Profile',
    top_nav=True,
    path='/Cluster_Profile'
)

# DATASET
try:
    df = pd.read_excel("New Model 6_Clusters.xlsx")
except Exception as e:
    df = pd.DataFrame()  # Fallback to an empty dataframe if loading fails
    print(f"Error loading dataset: {e}")

# Ensure 'Clusters' column is present
if 'Clusters' not in df.columns:
    cluster_columns = [col for col in df.columns if col.startswith('Clusters_')]
    if cluster_columns:
        df['Clusters'] = df[cluster_columns].idxmax(axis=1)
# Columns to display
numerical_columns = ['LT (m2)', 'Harga Tanah (m2)', 'Lebar Jalan Depan (m)', 'distance_ke_pusatkota']
categorical_columns = ['Peruntukan', 'Kondisi Wilayah Sekitar']
columns_to_display = ['Clusters'] + numerical_columns + categorical_columns

# Calculate mean values for numerical columns except 'Harga Tanah (m2)'
numerical_means = df.groupby('Clusters')[['LT (m2)', 'Lebar Jalan Depan (m)', 'distance_ke_pusatkota']].mean().reset_index()

# Format the numerical columns with commas and 2 decimal places
for col in ['LT (m2)', 'Lebar Jalan Depan (m)', 'distance_ke_pusatkota']:
    numerical_means[col] = numerical_means[col].apply(lambda x: f"{x:,.2f}")

# Calculate min and max values for 'Harga Tanah (m2)'
harga_tanah_min = df.groupby('Clusters')['Harga Tanah (m2)'].min().reset_index()
harga_tanah_max = df.groupby('Clusters')['Harga Tanah (m2)'].max().reset_index()

# Combine min and max values into a range string for 'Harga Tanah (m2)'
harga_tanah_range = harga_tanah_min.copy()
harga_tanah_range['Harga Tanah (m2)'] = harga_tanah_min['Harga Tanah (m2)'].astype(str) + " - " + harga_tanah_max['Harga Tanah (m2)'].astype(str)

# Format the 'Harga Tanah (m2)' column with commas and 2 decimal places
harga_tanah_range['Harga Tanah (m2)'] = harga_tanah_range['Harga Tanah (m2)'].apply(lambda x: f"{float(x.split(' - ')[0]):,.2f} - {float(x.split(' - ')[1]):,.2f}")

# Merge numerical means with the formatted 'Harga Tanah (m2)' range
cluster_means = pd.merge(numerical_means, harga_tanah_range[['Clusters', 'Harga Tanah (m2)']], on='Clusters')

# Calculate most frequent category for categorical columns
categorical_modes = df.groupby('Clusters')[categorical_columns].agg(lambda x: x.mode()[0]).reset_index()

# Merge numerical means and categorical modes
cluster_means = pd.merge(cluster_means, categorical_modes, on='Clusters')



layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            html.H1("Cluster Profiles"),
            html.Hr(),
            html.Div(id="cluster-profile-table"),
            dcc.Graph(id="cluster-profile-graph")
        ])
    ])
])

@callback(
    [Output("cluster-profile-table", "children"),
     Output("cluster-profile-graph", "figure")],
    [Input("url", "pathname")]
)
def update_cluster_profile(pathname):
    if df.empty:
        return "Dataset failed to load. Please try again later.", {}
    
    # Create table
    table_header = [
        html.Thead(html.Tr([html.Th(col) for col in columns_to_display]))
    ]
    table_body = [
        html.Tbody([
            html.Tr([html.Td(cluster_means.iloc[i][col]) for col in columns_to_display]) for i in range(len(cluster_means))
        ])
    ]
    
    # Create bar graph for numerical columns except 'Harga Tanah (m2)'
    fig = px.bar(cluster_means, x='Clusters', y=['LT (m2)', 'Lebar Jalan Depan (m)', 'distance_ke_pusatkota'], barmode='group', title="Values per Cluster")
    
    return dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, dark=True), fig
