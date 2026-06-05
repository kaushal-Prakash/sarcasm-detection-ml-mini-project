from ..ml.predictor import SarcasmPredictor

# Prediction Service with Emoji Strategy
class PredictionService:

    def __init__(self):
        self.predictor = SarcasmPredictor(strategy_type="emoji")

    def get_prediction(self, text):
        return self.predictor.predict(text)