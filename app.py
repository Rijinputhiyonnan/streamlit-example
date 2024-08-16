import streamlit as st
import pickle

model_file = open('model.pkl','rb')

model = pickle.load(model_file)
st.title('Bank note fraud prediction')

st.write('This is a bank note detection app')

variance = st.slider('Variance', 0,4)
skewness = st.number_input('Skeness value')
curtosis = st.number_input('Curtosis value')
entropy = st.number_input('Entropy value')



if st.button('Make prediction', type = 'primary') and variance!=None and skewness!=None and curtosis!=None and entropy!=None:
    import numpy as np
    input_features = np.array([[float(variance),float(skewness),float(curtosis),float(entropy)]])


predictions = model.predict(input_features)
st.write(predictions)
st.balloons()