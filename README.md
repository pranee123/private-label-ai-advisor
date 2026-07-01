# 🛒 AI-Powered Private Label Adoption Prediction & Recommendation System

## 📌 Project Overview

This project predicts retail stores that are most likely to adopt private label products using Machine Learning and provides AI-powered business recommendations using Google Gemini.

The solution combines Data Engineering, Machine Learning, Explainable AI (SHAP), Product Recommendation, and Generative AI into a single Streamlit application.

---

# Business Problem

Retail distributors want to increase the adoption of their private label products.

Instead of approaching every customer manually, this system predicts which stores are the most promising targets and recommends products that should be pitched.

---

# Features

- Store Adoption Prediction
- Opportunity Scoring
- Explainable AI (SHAP)
- Product Recommendation Engine
- AI Business Advisor
- Interactive Streamlit Dashboard

---

# Project Architecture

```
BigQuery Sales Data
        │
        ▼
Feature Engineering
        │
        ▼
Store-Level Dataset
        │
        ▼
XGBoost Classification Model
        │
        ▼
Adoption Probability
        │
        ▼
SHAP Explainability
        │
        ▼
Recommendation Engine
        │
        ▼
Streamlit Dashboard
        │
        ▼
Gemini AI Advisor
```

---

# Machine Learning Workflow

1. Data Extraction
2. Data Cleaning
3. Feature Engineering
4. Target Variable Creation
5. Model Training
6. Model Evaluation
7. Explainability using SHAP
8. Store Scoring
9. Product Recommendation
10. AI Recommendation Generation

---

# Technologies Used

## Programming

- Python
- SQL

## Data Engineering

- Google BigQuery
- Pandas
- NumPy

## Machine Learning

- XGBoost
- Scikit-Learn
- SHAP

## Dashboard

- Streamlit

## Generative AI

- Google Gemini API
- Prompt Engineering

## Version Control

- Git
- GitHub

---

# Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 91% |
| ROC AUC | 95% |

---

# Dashboard Pages

### Dashboard

Displays

- Total Stores
- Hot Opportunities
- Revenue Potential
- Top Opportunities

---

### Store Search

Search individual stores and view

- Adoption Probability
- Opportunity Segment
- Revenue Potential
- Store Statistics

---

### Recommendations

Displays recommended private label products.

---

### AI Advisor

Uses Gemini to generate

- Business Insights
- Sales Strategy
- Product Pitch Suggestions
- Expected Business Impact

---

# Folder Structure

```
private-label-ai-advisor/

│

├── app.py

├── advisor.py

├── requirements.txt

├── README.md

│

├── data/

│   ├── store_adoption_scores.csv

│   ├── store_product_history.csv

│   ├── top_100_opportunities.csv

│

├── pages/

│   ├── 1_Dashboard.py

│   ├── 2_Store_Search.py

│   ├── 3_Recommendations.py

│   └── 4_AI_Assistant.py
```

---

# Installation

```bash
git clone https://github.com/<your-username>/private-label-ai-advisor.git

cd private-label-ai-advisor

pip install -r requirements.txt

streamlit run app.py
```

---

# Future Improvements

- Multi-category prediction
- Demand Forecasting
- Dynamic Product Recommendation
- Agentic AI Workflow
- RAG-based Knowledge Assistant
- Sales Copilot
- Customer Churn Prediction

---

# Author

Praneeth Goud

AI / ML Developer
