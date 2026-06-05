from .model_loader import ModelLoader
from .model_factory import get_strategy
from .postprocessing import postprocess_prediction

class SarcasmPredictor:

    def __init__(self, strategy_type="text"):
        self.loader = ModelLoader()
        self.strategy = get_strategy(strategy_type)

    def predict(self, text):
        processed_text = self.strategy.process(text)

        vector = self.loader.vectorizer.transform([processed_text])
        prediction = self.loader.model.predict(vector)[0]
        proba = self.loader.model.predict_proba(vector)[0]

        return postprocess_prediction(prediction, proba, text)