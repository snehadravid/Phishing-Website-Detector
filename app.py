import streamlit as st
import joblib
from pathlib import Path
from datetime import datetime

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

# ---------------- INITIALIZE HISTORY ----------------

if "scan_history" not in st.session_state:
    st.session_state.scan_history = []

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

            if prediction == 0:
                result = "Potentially Phishing"
                st.error("⚠️ Potentially Phishing Website")
                st.write("Avoid entering passwords or personal information.")
            else:
                result = "Likely Legitimate"
                st.success("✅ Likely Legitimate Website")
                st.write("The model classifies this URL as legitimate.")

            st.metric("Model Confidence", f"{confidence:.2f}%")

            # Save scan in session history
            st.session_state.scan_history.insert(0, {
                "url": website_url,
                "result": result,
                "confidence": f"{confidence:.2f}%",
                "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })

            st.caption(
                "Confidence is the model's estimated probability, "
                "not a guarantee of website safety."
            )

        except Exception as error:
            st.error(f"Prediction error: {error}")

# ---------------- SCAN HISTORY ----------------

st.divider()

st.subheader("📜 Scan History")

if st.session_state.scan_history:

    for index, scan in enumerate(st.session_state.scan_history, start=1):

        with st.expander(f"Scan {index}: {scan['url']}"):

            st.write("**Website URL:**", scan["url"])
            st.write("**Result:**", scan["result"])
            st.write("**Confidence:**", scan["confidence"])
            st.write("**Scan Time:**", scan["time"])

    if st.button("🗑️ Clear Scan History"):
        st.session_state.scan_history = []
        st.rerun()

else:
    st.info("No scan history available. Scan a website to see its history.")

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