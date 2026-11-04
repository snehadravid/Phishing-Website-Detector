
import streamlit as st
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "phishing_model.pkl"

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.title("🛡️ Phishing Website Detector")

st.write(
    "Enter a website URL to check whether it is "
    "likely legitimate or potentially phishing."
)

st.warning(
    "This tool provides a machine-learning estimate. "
    "It cannot guarantee that a website is safe."
)

url = st.text_input(
    "Enter Website URL",
    placeholder="https://www.example.com"
)

if st.button("Check Website", type="primary"):

    if not url.strip():
        st.error("Please enter a website URL.")

    else:
        try:
            website_url = url.strip()

            if not website_url.startswith(("http://", "https://")):
                website_url = "https://" + website_url

            prediction = int(model.predict([website_url])[0])
            probabilities = model.predict_proba([website_url])[0]

            classes = list(model.classes_)
            confidence = probabilities[classes.index(prediction)] * 100

            if prediction == 0:
                st.error("⚠️ Potentially Phishing Website")
            else:
                st.success("✅ Likely Legitimate Website")

            st.write(f"Model confidence: {confidence:.2f}%")

            st.caption(
                "Confidence is the model's estimated probability, "
                "not a guarantee of website safety."
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")
