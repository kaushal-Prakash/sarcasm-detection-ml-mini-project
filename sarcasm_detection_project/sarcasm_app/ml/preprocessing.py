import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation and other symbols
    return text


def extract_emojis(text):
    # More general emoji detection
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.findall(text)


def preprocess_text(text):
    cleaned = clean_text(text)
    emojis = extract_emojis(text)

    return {
        "cleaned_text": cleaned,
        "emojis": emojis
    }