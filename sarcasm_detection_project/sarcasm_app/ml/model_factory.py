from .strategies import TextOnlyStrategy, EmojiStrategy

def get_strategy(strategy_type):
    if strategy_type == "emoji":
        return EmojiStrategy()
    return TextOnlyStrategy()