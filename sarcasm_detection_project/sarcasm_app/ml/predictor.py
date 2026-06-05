from .model_loader import ModelLoader
from .model_factory import get_strategy

class SarcasmPredictor:

    def __init__(self, strategy_type="text"):
        self.loader = ModelLoader()
        self.strategy = get_strategy(strategy_type)

    def predict(self, text):
        processed_text = self.strategy.process(text)

        vector = self.loader.vectorizer.transform([processed_text])
        prediction = self.loader.model.predict(vector)[0]

        # 🔥 Confidence
        proba = self.loader.model.predict_proba(vector)[0]
        confidence = max(proba)

        # 🔥 RULE-BASED BOOST (ADD HERE)
        if any(e in text for e in ["😒", "🙄", "😑"]):
            prediction = 1
            confidence = max(confidence, 0.75)  # boost confidence

        result = "Sarcastic" if prediction == 1 else "Not Sarcastic"

        return {
            "result": result,
            "confidence": float(round(confidence * 100, 2))
        }