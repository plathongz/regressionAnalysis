
# Step 1: Import libraries
import streamlit as st
import pandas as pd
import pickle

# App title
st.title("💡 Sales Prediction App")

# Step 2: Load the model
model_file = "model-reg-67130701704.pkl"

try:
    with open(model_file, "rb") as file:
        model = pickle.load(file)
    st.success(f"✅ Model loaded successfully: {model_file}")
except FileNotFoundError:
    st.error(f"❌ Model file '{model_file}' not found.")
    st.stop()

# Step 3: Input section — user enters data from webpage
st.header("Enter Advertising Budget")

youtube = st.number_input("YouTube budget", min_value=0.0, value=50.0)
tiktok = st.number_input("TikTok budget", min_value=0.0, value=50.0)
instagram = st.number_input("Instagram budget", min_value=0.0, value=50.0)

# Step 4: Create a new DataFrame from user input
new_data = pd.DataFrame({
    "youtube": [youtube],
    "tiktok": [tiktok],
    "instagram": [instagram]
})

# Step 5: Predict when user clicks button
if st.button("Predict Sales"):
    predicted_sales = model.predict(new_data)
    st.subheader("📊 Estimated Sales:")
    st.write(round(predicted_sales[0], 2))
