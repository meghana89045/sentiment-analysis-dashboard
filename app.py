import streamlit as st
import pandas as pd
from model.sentiment_model import load_model, analyze_batch
from utils.preprocess import clean_batch
from utils.visualize import plot_sentiment_pie, plot_confidence_bar, plot_wordcloud

# Page config
st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="💬",
    layout="wide"
)

# Load model (cached so it loads only once)
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# ---- HEADER ----
st.title("💬 Sentiment Analysis Dashboard")
st.markdown("Analyze sentiment of reviews or any text using **DistilBERT**")
st.divider()

# ---- SIDEBAR ----
st.sidebar.title("⚙️ Options")
input_mode = st.sidebar.radio(
    "Choose Input Mode",
    ["✍️ Type Text", "📄 Upload CSV"]
)

# ---- INPUT MODE 1: Type Text ----
if input_mode == "✍️ Type Text":
    st.subheader("✍️ Enter your text below")
    user_input = st.text_area(
        "One review per line:",
        height=200,
        placeholder="I love this product!\nThis was terrible.\nIt was okay I guess."
    )

    if st.button("🔍 Analyze"):
        if user_input.strip():
            with st.spinner("Analyzing sentiment..."):
                texts = user_input.strip().split("\n")
                cleaned = clean_batch(texts)
                results = analyze_batch(cleaned, model)
                df = pd.DataFrame(results)

            st.success(f"✅ Analyzed {len(df)} reviews!")
            st.divider()

            # ---- METRICS ----
            col1, col2, col3 = st.columns(3)
            positive = len(df[df["label"] == "POSITIVE"])
            negative = len(df[df["label"] == "NEGATIVE"])
            avg_score = round(df["score"].mean(), 2)

            col1.metric("😊 Positive", positive)
            col2.metric("😞 Negative", negative)
            col3.metric("📊 Avg Confidence", f"{avg_score}%")

            st.divider()

            # ---- CHARTS ----
            col4, col5 = st.columns(2)
            with col4:
                st.plotly_chart(plot_sentiment_pie(df), use_container_width=True)
            with col5:
                st.plotly_chart(plot_confidence_bar(df), use_container_width=True)

            # ---- WORD CLOUD ----
            st.subheader("☁️ Word Cloud")
            st.pyplot(plot_wordcloud(cleaned))

            # ---- RAW DATA ----
            st.subheader("📋 Detailed Results")
            st.dataframe(df, use_container_width=True)

        else:
            st.warning("⚠️ Please enter some text first!")

# ---- INPUT MODE 2: Upload CSV ----
elif input_mode == "📄 Upload CSV":
    st.subheader("📄 Upload a CSV file")
    st.info("CSV must have a column named **'text'**")

    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file:
        df_input = pd.read_csv(uploaded_file)

        if "text" not in df_input.columns:
            st.error("❌ CSV must have a 'text' column!")
        else:
            st.write(f"📂 Loaded **{len(df_input)}** rows")
            st.dataframe(df_input.head(), use_container_width=True)

            if st.button("🔍 Analyze"):
                with st.spinner("Analyzing sentiment..."):
                    texts = df_input["text"].tolist()
                    cleaned = clean_batch(texts)
                    results = analyze_batch(cleaned, model)
                    df = pd.DataFrame(results)

                st.success(f"✅ Analyzed {len(df)} reviews!")
                st.divider()

                # ---- METRICS ----
                col1, col2, col3 = st.columns(3)
                positive = len(df[df["label"] == "POSITIVE"])
                negative = len(df[df["label"] == "NEGATIVE"])
                avg_score = round(df["score"].mean(), 2)

                col1.metric("😊 Positive", positive)
                col2.metric("😞 Negative", negative)
                col3.metric("📊 Avg Confidence", f"{avg_score}%")

                st.divider()

                # ---- CHARTS ----
                col4, col5 = st.columns(2)
                with col4:
                    st.plotly_chart(plot_sentiment_pie(df), use_container_width=True)
                with col5:
                    st.plotly_chart(plot_confidence_bar(df), use_container_width=True)

                # ---- WORD CLOUD ----
                st.subheader("☁️ Word Cloud")
                st.pyplot(plot_wordcloud(cleaned))

                # ---- RAW DATA ----
                st.subheader("📋 Detailed Results")
                st.dataframe(df, use_container_width=True)