#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 09:21:23 2017

@author: eliza_mitchell
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

app = dash.Dash()

df = pd.read_csv('planet_data.csv', usecols = ['Object','Carbon Dioxide','Nitrogen','Oxygen','Argon','Methane','Sodium','Hydrogen','Helium','Other'])
df.fillna(0, inplace=True)
cols = ['Carbon Dioxide','Nitrogen','Oxygen','Argon','Methane','Sodium','Hydrogen','Helium','Other']
df[cols] = df[cols].replace({'%':'', '<':''}, regex = True)
df[cols] = df[cols].apply(pd.to_numeric)

app.layout = html.Div(children=[
    html.H1(children='Planetary Atomospheres'),
    dcc.Graph(
        id = 'planet-atmo-scatter',
        figure = go.Figure(
            data = [
                go.Bar(
                    x = cols,
                    y = df[cols].loc[i],
                    name = df.iloc[i][0],
                    marker = go.Marker(
                        color = 'rgb(, 83, 109)'
                    )
                ) for i in range(0, len(df.index))
            ],
            layout=go.Layout(
                title='Planetary Atmospheres',
                showlegend=True,
                legend=go.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.Margin(l=40, r=0, t=40, b=30)
            )
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
