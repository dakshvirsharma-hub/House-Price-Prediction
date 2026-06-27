import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

# New house
new_house = pd.DataFrame({
    "longitude": [-122.23],
    "latitude": [37.88],
    "housing_median_age": [41],
    "total_rooms": [880],
    "total_bedrooms": [129],
    "population": [322],
    "households": [126],
    "median_income": [2.3252],
    "avg_rooms_per_household": [880/126],
    "avg_bedrooms_per_room": [129/880],
    "avg_population_per_household": [322/126]
})

prediction = model.predict(new_house)

print("Predicted House Price:", prediction[0])