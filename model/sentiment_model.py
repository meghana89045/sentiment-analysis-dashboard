from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

# Load the model once (cached after first run)
def load_model():
    model = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
        truncation=True,
        max_length=512
    )
    return model

# Analyze a single text
def analyze_sentiment(text, model):
    result = model(text)[0]
    label = result["score"]
    score = result["score"]
    return {
        "label": result["label"],   # POSITIVE / NEGATIVE
        "score": round(score * 100, 2)  # confidence %
    }

# Analyze a list of texts
def analyze_batch(texts, model):
    results = []
    for text in texts:
        if text.strip():  # skip empty lines
            sentiment = analyze_sentiment(text, model)
            results.append({
                "text": text,
                "label": sentiment["label"],
                "score": sentiment["score"]
            })
    return results
if __name__ == "__main__":
    print("Loading model...")
    model = load_model()
    print("Model loaded!")

    test_texts = [
        "I love this product, it's amazing!",
        "This is the worst experience ever.",
        "It was okay, nothing special."
    ]

    results = analyze_batch(test_texts, model)
    for r in results:
        print(f"Text: {r['text']}")
        print(f"Sentiment: {r['label']} | Confidence: {r['score']}%")
        print("---")