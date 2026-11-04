\# Phishing Website Detector



A machine learning-based web application that detects potentially phishing websites using URL patterns.



\## Features

\- Enter a website URL.

\- Predict whether it is likely legitimate or potentially phishing.

\- Display the model's prediction confidence.

\- Simple and interactive Streamlit interface.



\## Technologies Used

\- Python

\- Streamlit

\- Scikit-learn

\- TF-IDF Vectorizer

\- SGD Classifier



\## Project Structure

```text

PhishingWebsiteDetector/

├── app.py

├── requirements.txt

├── models/

│   └── phishing\_model.pkl

└── src/

&#x20;   ├── feature\_extraction.py

&#x20;   └── train\_model.py

```



\## Run Locally



Install dependencies:



```bash

pip install -r requirements.txt

```



Start the application:



```bash

python -m streamlit run app.py

```



\## Disclaimer

This application provides machine-learning estimates and cannot guarantee that a website is safe.

