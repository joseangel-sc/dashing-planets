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
df[cols] = df[cols].replace({'%':'', '<': ''}, regex = True)
df[cols] = df[cols].apply(pd.to_numeric)

print(df)
