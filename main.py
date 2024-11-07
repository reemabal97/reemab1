import numpy as np
import pandas as pd
import streamlit as st

st.title("This is first Assignment")
st.write("This assignment is for cloud computing")

data = pd.DataFrame({
    "C1": ['A','B','C','D','E'],
    "C2": [100, 200, 300, 400, 500]
})
st.write("This is just a sample data")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 4),
    columns=['P', 'Q','R','T']
)

st.bar_chart(chart_data)