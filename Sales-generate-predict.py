import streamlit as st
import pandas as pd
import seaborn as sns
import pickle
from sklearn.svm import SVR


st.write("# Simple Sale Prediction App")
st.write("This app predicts the **Sale** base on Advertisement Channel's Effort!")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.0,50.0,100.0)
    Radio = st.sidebar.slider('Radio', 0.0,50.0,100.00)
    Newspaper = st.sidebar.slider('Newspaper',0.0,50.0,100.00)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

Modelsales = pickle.load(open("modelflights.h5", "rb")) 

prediction = Modelsales.predict(df)


st.subheader('Prediction')
st.write(prediction)


