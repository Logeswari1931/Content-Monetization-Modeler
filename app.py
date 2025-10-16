import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('linear_regression_model.pkl')

st.title("YouTube Ad Revenue Prediction")

# Numeric inputs
st.header("Numeric Features")
views = st.number_input("Views", min_value=0)
likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)
watch_time_minutes = st.number_input("Watch Time (minutes)", min_value=0)
video_length_minutes = st.number_input("Video Length (minutes)", min_value=0)
subscribers = st.number_input("Subscribers", min_value=0)
revenue_per_view = st.number_input("Revenue per View", min_value=0.0, format="%.2f")
watch_time_per_view = st.number_input("Watch Time per View", min_value=0.0, format="%.2f")
watch_to_length_ratio = st.number_input("Watch to Length Ratio", min_value=0.0, format="%.2f")
engagement_rate = st.number_input("Engagement Rate", min_value=0.0, format="%.2f")

# Categorical inputs
st.header("Categorical Features")
category = st.selectbox("Category", ["Tech", "Gaming", "Music", "Lifestyle", "Entertainment"])
device = st.selectbox("Device", ["Mobile", "Tablet", "TV"])
country = st.selectbox("Country", ["IN", "US", "UK", "CA", "DE"])

# Prepare input dataframe with all one-hot encoded columns
# List all possible one-hot columns used in training
all_columns = model.feature_names_in_  # Get columns from trained model
input_dict = {
    'views': views,
    'likes': likes,
    'comments': comments,
    'watch_time_minutes': watch_time_minutes,
    'video_length_minutes': video_length_minutes,
    'subscribers': subscribers,
    'revenue_per_view': revenue_per_view,
    'watch_time_per_view': watch_time_per_view,
    'watch_to_length_ratio': watch_to_length_ratio,
    'engagement_rate': engagement_rate,
    # One-hot encoding categorical manually
    'category_Tech': 1 if category=="Tech" else 0,
    'category_Gaming': 1 if category=="Gaming" else 0,
    'category_Music': 1 if category=="Music" else 0,
    'category_Lifestyle': 1 if category=="Lifestyle" else 0,
    'category_Entertainment': 1 if category=="Entertainment" else 0,
    'device_Mobile': 1 if device=="Mobile" else 0,
    'device_Tablet': 1 if device=="Tablet" else 0,
    'device_TV': 1 if device=="TV" else 0,
    'country_IN': 1 if country=="IN" else 0,
    'country_US': 1 if country=="US" else 0,
    'country_UK': 1 if country=="UK" else 0,
    'country_CA': 1 if country=="CA" else 0,
    'country_DE': 1 if country=="DE" else 0
}

# Create dataframe in same column order as training
input_df = pd.DataFrame([input_dict], columns=all_columns)

# Predict button
if st.button("Predict Ad Revenue"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Ad Revenue: ${prediction[0]:.2f}")