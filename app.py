import streamlit as st
import pandas as pd
import joblib

model  = joblib.load("house_price_model.pkl")


st.title("House price predicition by Daksh 🏡")
st.markdown ("This is a simple web app to predict house prices based on various features. Please enter the details below and click on the 'Predict' button to get the predicted price.")


longitude = st.number_input("Longitude", -124.35, -114.31, -122.23)

latitude = st.number_input("Latitude", 32.54, 41.95, 37.88)

housing_median_age = st.slider("House Age", 1, 52, 29)

total_rooms = st.number_input("Total Rooms in the block ", 2, 39320, 2635)

total_bedrooms = st.number_input("Total Bedrooms in the area ", 1, 6445, 537)

population = st.number_input("Population in the area", 3, 35682, 1425)

households = st.number_input("Households in the sector", 1, 6082, 499)

median_income = st.number_input("Median Income in $K/month", 0.4999, 15.0001, 3.87)
if st.button("Predict Price"):

    avg_rooms_per_household = total_rooms / households
    avg_bedrooms_per_room = total_bedrooms / total_rooms
    avg_population_per_household = population / households

    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "avg_rooms_per_household": [avg_rooms_per_household],
        "avg_bedrooms_per_room": [avg_bedrooms_per_room],
        "avg_population_per_household": [avg_population_per_household]
    })

    prediction = model.predict(input_data)

    st.success(f"🏠 Estimated House Price: ${prediction[0]:,.2f}")