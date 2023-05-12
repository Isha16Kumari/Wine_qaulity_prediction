# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:59:15 2023

@author: dell
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/dell/OneDrive/Desktop/Wine/Wine_quality.sav', 'rb'))


# creating a function for Prediction

def wine_quality(input_data):
    

    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the data as we are predicting the label for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1):
       return print('Good Quality Wine')
    else:  
       return print('Bad Quality Wine')
  
    
  
def main():
    
    
    # giving a title
    st.title('WINE QUALITY PREDICTION Web App')
    
    
    # getting the input data from the user
    
    
    fixedacidity = st.text_input('Acidity Value')
    volatileacidity = st.text_input('Volatile Level')
    citricacid = st.text_input('Citirc acid value')
    residualsugar  = st.text_input('Residual sugar value')
    chlorides = st.text_input('chlorides Level')
    freesulphur = st.text_input('free sulphur value')
    totalsulphur = st.text_input('total sulphur value')
    density = st.text_input('density of wine')
    pH = st.text_input('ph level')
    sulphates = st.text_input('sulphate')
    alcohol = st.text_input('alcohol amount')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Wine quality Test Result'):
        diagnosis = wine_quality([fixedacidity, volatileacidity, citricacid, residualsugar, chlorides, freesulphur, totalsulphur, density, pH, sulphates, alcohol])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()