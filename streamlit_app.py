import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import argparse
import sys
from binance.spot import Spot as BinClient

from bokeh.models import BoxAnnotation
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.sampledata.sprint import sprint

Bin_API_Key  = "3NQ3eBCvOnTDpmkO6yOI7SkqoKvLhpF2ddFyaYWEQf0QmLyweQgx6Oyw62q5xNC9"
Bin_API_Secret = "YcOEDE19tnJIRZJxgI9hEugVmha4grCrEXDCJH7kNRJtdIwN38QO9FjFc71n636c"

dict_params = st.experimental_get_query_params()
args = dict_params['coin']

if dict_params['coin'][0]=="abc": 
    st.write('Hello, ABC!')
else: 
    st.write('Hello, ELSE!')
    
st.write(dict_params)
st.write(dict_params['coin'])
st.write(dict_params['coin'][0])
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.line_chart(chart_data)



df = sprint.copy()  # since we are modifying sampledata

df.Year = df.Year.astype(str)
group = df.groupby('Year')
source = ColumnDataSource(group)

p = figure(y_range=group, x_range=(9.5,12.7), width=400, height=550, toolbar_location=None,
           title="Time Spreads for Sprint Medalists (by Year)")
p.hbar(y="Year", left='Time_min', right='Time_max', height=0.4, source=source)

p.ygrid.grid_line_color = None
p.xaxis.axis_label = "Time (seconds)"
p.outline_line_color = None

st.bokeh_chart(p, use_container_width=True)



spot_client = BinClient(base_url="https://testnet.binance.vision")
data1 = pd.DataFrame(spot_client.historical_trades("BTCUSDT", limit=10, fromId="100"))
st.line_chart(data1, x="time", y="price")




st.button("Reset1", type="primary")
st.button("Reset2", type="secondary")


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)





