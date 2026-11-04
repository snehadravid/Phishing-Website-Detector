# 🛡️ Phishing Website Detector

An AI-powered web application that uses Machine Learning to detect potentially phishing websites by analyzing URL patterns.

🌐 **Live Demo:** [Try the Phishing Website Detector](https://phishing-website-detector-xc4qfswctznshm3nqovwa2.streamlit.app/)

## 📌 About the Project

Phishing is a common cybersecurity threat in which attackers create fake websites to steal sensitive information such as passwords, banking details, and personal data.

This project uses a trained Machine Learning model to classify website URLs into two categories:

- ✅ Likely Legitimate
- ⚠️ Potentially Phishing

The application provides an easy-to-use interface where users can enter a URL, scan it, view the prediction confidence, and review their scan history.

## ✨ Features

- 🔍 Website URL scanning
- 🤖 Machine Learning-based phishing detection
- 📊 Prediction confidence percentage
- 📜 Scan history
- 🗑️ Clear scan history option
- 🎨 Professional dark-blue user interface
- 🌐 Online deployment using Streamlit Community Cloud

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Dataset processing |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | URL text feature extraction |
| SGD Classifier | Classification algorithm |
| Joblib | Model saving and loading |
| Streamlit | Web application |
| GitHub | Version control and hosting |

## 🧠 Machine Learning Workflow

1. Load and prepare the phishing URL dataset.
2. Extract URL text for model training.
3. Convert URL text into numerical features using character-level TF-IDF.
4. Train an SGDClassifier model.
5. Evaluate the model using a test dataset.
6. Save the trained model.
7. Load the model into the Streamlit application to predict new URLs.

**Reported test accuracy: approximately 99.41%.**

This is the result on the project's held-out test dataset. Real-world performance may differ.

## 📂 Project Structure

```text
PhishingWebsiteDetector/
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── PhiUSIIL_Phishing_URL_Dataset.csv
│
├── models/
│   └── phishing_model.pkl
│
└── src/
    ├── feature_extraction.py
    └── train_model.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/snehadravid/Phishing-Website-Detector.git
```

### 2. Open the project folder

```bash
cd Phishing-Website-Detector
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install the required libraries

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local application at:

`http://localhost:8501`

## 🚀 Live Application

Try the deployed project here:

👉 [Phishing Website Detector – Live Demo](https://phishing-website-detector-xc4qfswctznshm3nqovwa2.streamlit.app/)

## 📸 Application Preview

*Add screenshots of your website here to show the user interface, prediction results, and scan history.*

## 🔐 Security Disclaimer

This project is developed for educational and demonstration purposes.

- Predictions are machine-learning estimates.
- A legitimate classification does not guarantee that a website is safe.
- A phishing classification is not a definitive security verdict.
- Never share passwords or sensitive information based only on this application.

## 🔮 Future Enhancements

- Permanent scan history using a database.
- Real-time threat intelligence integration.
- Advanced URL and domain analysis.
- Improved model evaluation using unseen real-world URLs.
- Detailed scan reports and visual analytics.

## 👩‍💻 Author

**Snehadravid**

GitHub: [@snehadravid](https://github.com/snehadravid)

---

⭐ If you find this project interesting, consider giving the repository a star!

**Phishing Website Detector | Machine Learning | Cybersecurity**
