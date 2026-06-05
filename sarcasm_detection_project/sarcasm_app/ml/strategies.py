from .preprocessing import preprocess_text

# Preprocessing Strategies for Sarcasm Detection

class PreprocessingStrategy:
    def process(self, text):
        raise NotImplementedError

# Two strategies: TextOnly and Emoji-Enhanced
class TextOnlyStrategy(PreprocessingStrategy):
    def process(self, text):
        data = preprocess_text(text)
        return data["cleaned_text"]

# Emoji strategy that combines cleaned text with extracted emojis
class EmojiStrategy(PreprocessingStrategy):
    def process(self, text):
        data = preprocess_text(text)
        emoji_text = " ".join(data["emojis"])
        return f"{data['cleaned_text']} {emoji_text}".strip()