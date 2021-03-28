# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:36:33 2021

@author: Lenovo
"""
from bokeh.plotting import figure, output_notebook, show 
from bokeh.models.tools import HoverTool
import streamlit as st


def app():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    
    p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')
    
    p.line(x, y, legend_label='Trend', line_width=2)
    
    st.bokeh_chart(p)