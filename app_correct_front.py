import streamlit as st
import requests

st.set_page_config(page_title="🎬 Movie Success Forecaster", page_icon="🎥")

st.title("🎬 Movie Success Forecaster")
st.write("Enter a movie name and one or more user reviews to forecast its success!")

movie = st.text_input("Enter Movie Title")
review = st.text_area("Paste a User Review")

if st.button("Predict Success"):
    try:
        res = requests.post(
            "https://movie-api.onrender.com/predict",  # Replace with your actual Render URL
            json={"movie": movie, "review": review},
            timeout=10,
        )
        if res.status_code == 200:
            result = res.json()
            st.success(
                f"**Movie:** {result['movie']}  \n"
                f"**Prediction:** {result['prediction']}  \n"
                f"**Confidence:** {result['confidence']}"
            )
        else:
            st.error(f"Server returned error code: {res.status_code}")
    except Exception as e:
        st.error(f"❌ Could not connect to backend API. Error: {e}")
