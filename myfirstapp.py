import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Streamlit App")
st.write(pd.DataFrame({
    'Students': ['John', 'Lofa', 'Siti', 'Amy', 'Luke', 'Herda', 'Gajen'],
    'Attendance Status': ['no', 'yes', 'no', 'no', 'yes', 'yes','yes']
}))
