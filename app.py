
import streamlit as st
import joblib
from pathlib import Path

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "phishing_model.pkl"

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #071526, #102b46);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 16px;
    margin-bottom: 30px;
}

div.stButton > button {
    width: 100%;
    background: #0284c7;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #0369a1;
    color: white;
}

.result-card {
    padding: 22px;
    border-radius: 14px;
    background: #173653;
    text-align: center;
    margin-top: 20px;
    border: 1px solid #315675;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()

# ---------------- WEBSITE HEADER ----------------

st.markdown(
    '<div class="main-title">🛡️ Phishing Website Detector</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered website security analysis</div>',
    unsafe_allow_html=True
)

st.info(
    "Enter a website URL below to check whether it is "
    "likely legitimate or potentially phishing."
)

# ---------------- URL INPUT ----------------

url = st.text_input(
    "🌐 Enter Website URL",
    placeholder="https://www.example.com"
)

# ---------------- PREDICTION ----------------

if st.button("🔍 Scan Website"):

    if not url.strip():
        st.warning("Please enter a website URL.")

    else:
        website_url = url.strip()

        if not website_url.startswith(("http://", "https://")):
            website_url = "https://" + website_url

        try:
            prediction = int(model.predict([website_url])[0])
            probabilities = model.predict_proba([website_url])[0]

            classes = list(model.classes_)
            confidence = probabilities[classes.index(prediction)] * 100

            st.markdown('<div class="result-card">', unsafe_allow_html=True)

            if prediction == 0:
                st.error("⚠️ Potentially Phishing Website")
                st.write("Avoid entering passwords or personal information.")
            else:
                st.success("✅ Likely Legitimate Website")
                st.write("The model classifies this URL as legitimate.")

            st.metric("Model Confidence", f"{confidence:.2f}%")

            st.markdown('</div>', unsafe_allow_html=True)

            st.caption(
                "Confidence is the model's estimated probability, "
                "not a guarantee of website safety."
            )

        except Exception as error:
            st.error(f"Prediction error: {error}")

# ---------------- SAFETY INFORMATION ----------------

st.divider()

st.subheader("🔐 Security Information")

st.write("""
- Checks URL patterns using a trained machine-learning model.
- Provides a prediction and estimated confidence.
- Does not guarantee that a website is safe.
- Never enter sensitive information based only on this result.
""")

st.markdown("""
<div class="footer">
    Phishing Website Detector | Machine Learning Project
</div>
""", unsafe_allow_html=True)
