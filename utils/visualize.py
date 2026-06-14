import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Pie chart - sentiment distribution
def plot_sentiment_pie(df):
    counts = df["label"].value_counts().reset_index()
    counts.columns = ["Sentiment", "Count"]
    fig = px.pie(
        counts,
        names="Sentiment",
        values="Count",
        color="Sentiment",
        color_discrete_map={
            "POSITIVE": "#2ecc71",
            "NEGATIVE": "#e74c3c"
        },
        title="Sentiment Distribution"
    )
    return fig

# Bar chart - confidence scores
def plot_confidence_bar(df):
    fig = px.bar(
        df,
        x=df.index,
        y="score",
        color="label",
        color_discrete_map={
            "POSITIVE": "#2ecc71",
            "NEGATIVE": "#e74c3c"
        },
        title="Confidence Scores per Review",
        labels={"score": "Confidence (%)", "index": "Review #"}
    )
    return fig

# Word cloud
def plot_wordcloud(texts):
    combined = " ".join(texts)
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="RdYlGn"
    ).generate(combined)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    ax.set_title("Most Frequent Words", fontsize=16)
    return fig
if __name__ == "__main__":
    sample = "Check out https://example.com! @john loved #AI so much!!!"
    print("Before:", sample)
    print("After:", clean_text(sample))