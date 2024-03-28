# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:20:03 2024

@author: daffa
"""
from dash import html, register_page, dash_table
import pandas as pd 
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output #, callback # If you need callbacks, import it here.
import dash_bootstrap_components as dbc

register_page(
    __name__,
    name='Geospatial',
    top_nav=True,
    path='/Geospatial'
)

# DATASET
df = pd.read_excel("data aws.xlsx")

# MAPBOX CHART FUNCTION
def create_map_chart(df):
    figure = px.scatter_mapbox(
        df, 
        lat='latitude', 
        lon='longitude', 
        color='Clusters',
        title='Geospatial Analysis',
        mapbox_style="carto-positron",
        zoom=10,
        center={"lat": df['latitude'].mean(), "lon": df['longitude'].mean()},
    )
    figure.update_layout(height=720, width=1280)
    return figure

# FILTER OPTIONS
peruntukan_options = [{'label': peruntukan, 'value': peruntukan} for peruntukan in df['Peruntukan'].unique()]
kondisi_wilayah_options = [{'label': kondisi, 'value': kondisi} for kondisi in df['Kondisi Wilayah Sekitar'].unique()]
air_options = [{'label': air, 'value': air} for air in df['Air'].unique()]
listrik_options = [{'label': listrik, 'value': listrik} for listrik in df['Listrik'].unique()]
# Add more options for other columns as needed

# WIDGETS
peruntukan_dropdown = dcc.Dropdown(id='peruntukan-filter-dropdown', options=peruntukan_options, value=None, placeholder='Select Peruntukan')
kondisi_wilayah_dropdown = dcc.Dropdown(id='kondisi-ws-dropdown', options=kondisi_wilayah_options, value=None, placeholder='Select Kondisi Wilayah')
air_dropdown = dcc.Dropdown(id='ada-air-dropdown', options=air_options, value=None, placeholder='Select Air')
listrik_dropdown = dcc.Dropdown(id='ada-listrik-dropdown', options=listrik_options, value=None, placeholder='Select Listrik')


# PAGE LAYOUT
layout = html.Div(children=[
    html.H3('Geospatial Analysis'),
    dbc.Row([
        dbc.Col(peruntukan_dropdown, width=3),
        dbc.Col(kondisi_wilayah_dropdown, width=3),
        dbc.Col(air_dropdown, width=3),
        dbc.Col(listrik_dropdown, width=3)
 
    ]),
    dcc.Graph(id="map_chart")
])

# CALLBACKS
@callback(
    Output('map_chart', 'figure'),
    [Input('peruntukan-filter-dropdown', 'value'),
     Input('kondisi-ws-dropdown', 'value'),
     Input('ada-air-dropdown', 'value'),
     Input('ada-listrik-dropdown', 'value'),
     ]
    
)
def update_map(peruntukan_value, kondisi_wilayah_value, air_value, listrik_value):
    filtered_df = df.copy()
    if peruntukan_value:
        filtered_df = filtered_df[filtered_df['Peruntukan'] == peruntukan_value]
    if kondisi_wilayah_value:
        filtered_df = filtered_df[filtered_df['Kondisi Wilayah Sekitar'] == kondisi_wilayah_value]
    if air_value:
        filtered_df = filtered_df[filtered_df['Air'] == air_value]
    if listrik_value:
        filtered_df = filtered_df[filtered_df['Listrik'] == listrik_value]
    
    return create_map_chart(filtered_df)
