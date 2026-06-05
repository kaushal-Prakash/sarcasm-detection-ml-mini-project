from .preprocessing import preprocess_text

class PreprocessingStrategy:
    def process(self, text):
        raise NotImplementedError


class TextOnlyStrategy(PreprocessingStrategy):
    def process(self, text):
        data = preprocess_text(text)
        return data["cleaned_text"]


class EmojiStrategy(PreprocessingStrategy):
    def process(self, text):
        data = preprocess_text(text)
        emoji_text = " ".join(data["emojis"])
        return f"{data['cleaned_text']} {emoji_text}".strip()