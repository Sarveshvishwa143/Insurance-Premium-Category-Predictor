# 🧠 Insurance Premium Category Predictor

An end-to-end Machine Learning web application that predicts insurance premium categories using user lifestyle, demographic, and financial data.

Built with a production-style architecture:

* ⚡ FastAPI (Backend API)
* 🎯 Streamlit (Frontend UI)
* 🧠 Scikit-learn (ML Model)
* 🐼 Pandas (Data Processing)

---

## 🚀 Features

* Real-time prediction via REST API
* Interactive Streamlit UI with popup results
* Automatic feature engineering using Pydantic
* Confidence score + probability distribution
* Clean modular backend–frontend separation

---

## 🧩 Project Structure

.
├── app.py
├── frontend.py
├── model1.pkl
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Sarveshvishwa143/Insurance-Premium-Category-Predictor
cd insurance-premium-predictor
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

### Start FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend runs at:
http://127.0.0.1:8000

---

### Start Streamlit Frontend

```bash
streamlit run frontend.py
```

Frontend runs at:
http://localhost:8501

---

## 🔌 API Endpoint

### POST `/predict`

#### Request Example

```json
{
  "age": 30,
  "weight": 70,
  "height": 170,
  "income_lpa": 10,
  "smoker": true,
  "city": "Delhi",
  "occupation": "Software Engineer"
}
```

#### Response Example

```json
{
  "predicted_category": "medium",
  "confidence": 0.82,
  "class_probabilities": {
    "0": 0.1,
    "1": 0.82,
    "2": 0.08
  }
}
```

---

## 🧠 Feature Engineering

Handled dynamically in backend:

* BMI calculation
* Lifestyle risk classification
* Age grouping
* City tier classification
* Income segmentation

---

## 📊 Model Details

* Algorithm: Scikit-learn model (e.g., Random Forest)
* Supports probability prediction (`predict_proba`)
* Works on engineered + categorical features

---

## ⚠️ Important Notes

* Ensure `model1.pkl` is present in project root
* API must be running before frontend
* Model should include preprocessing pipeline (encoding, scaling)

---

## 🔥 Future Improvements

* Docker containerization
* Cloud deployment (Render / Railway)
* Authentication system
* Prediction logging
* Model explainability (SHAP)

---

## 👨‍💻 Author

Sarvesh
AI/ML + Backend Developer
