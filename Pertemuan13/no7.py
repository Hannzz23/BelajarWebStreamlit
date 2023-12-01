import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    #inisiasi nilai acak dengan 10 baris dan 2 kolom
    np.random.randn(10,2),
    columns=['x', 'y']
)

st.write('Below is DataFrame Line Chart')
st.line_chart(df)

st.write('Below is DataFrame Bar Chart')
st.bar_chart(df)

st.write('Below is DataFrame Area Chart')
st.area_chart(df)
