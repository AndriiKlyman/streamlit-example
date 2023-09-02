import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.button("Reset1", type="primary")
st.button("Reset2", type="secondary")
st.button("Reset3", type="secondary")
st.button("Reset4", type="secondary")
st.button("Reset5", type="secondary")

st.line_chart(chart_data)
