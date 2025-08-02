import streamlit as st
import numpy as np
import pickle


with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("House Price Prediction App")

st.write("""
### Enter the house details:
""")


gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=100, max_value=10000, value=1500)
bedroom_abv_gr = st.number_input("Number of Bedrooms Above Ground", min_value=0, max_value=10, value=3)
full_bath = st.number_input("Number of Full Bathrooms", min_value=0, max_value=5, value=2)


if st.button("Predict Sale Price"):
    input_data = np.array([[gr_liv_area, bedroom_abv_gr, full_bath]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Sale Price: ${prediction:,.2f}")
