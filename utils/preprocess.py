import re

def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove mentions (@user)
    text = re.sub(r"@\w+", "", text)
    # Remove hashtags
    text = re.sub(r"#\w+", "", text)
    # Remove special characters & numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    # Remove extra spaces
    text = text.strip().lower()
    return text

def clean_batch(texts):
    return [clean_text(t) for t in texts if t.strip()]

def split_into_sentences(text):
    # Split paragraph into individual sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]
if __name__ == "__main__":
    sample = "Check out https://example.com! @john loved #AI so much!!!"
    print("Before:", sample)
    print("After:", clean_text(sample))