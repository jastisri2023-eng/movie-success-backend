import streamlit as st
import requests

st.title("🎬 Movie Success Forecaster")
movie = st.text_input("Enter Movie Title")
review = st.text_area("Paste a User Review")

if st.button("Predict Success"):
    res = requests.post("http://127.0.0.1:8000/predict", json={"movie": movie, "review": review})
    result = res.json()
    st.success(f"Predicted Result: {result['prediction']} (Confidence: {result['confidence']})")
