# 💬 Sentiment Analysis Dashboard

A real-time sentiment analysis dashboard built with DistilBERT and Streamlit.

## 🚀 Features
- Analyze sentiment of any text (Positive/Negative)
- Upload CSV files for batch analysis
- Interactive pie charts, bar charts, and word clouds
- Confidence scores for each prediction

## 🛠️ Tech Stack
- **Model:** DistilBERT (HuggingFace Transformers)
- **Dashboard:** Streamlit
- **Visualizations:** Plotly, WordCloud, Matplotlib
- **Language:** Python

## ⚙️ Setup & Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-analysis-dashboard.git
cd sentiment-analysis-dashboard
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 📊 Usage
1. Type reviews (one per line) OR upload a CSV with a `text` column
2. Click Analyze
3. View sentiment breakdown with charts