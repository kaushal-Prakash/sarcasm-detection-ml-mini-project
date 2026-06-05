from ..ml.predictor import SarcasmPredictor

class PredictionService:

    def __init__(self):
        self.predictor = SarcasmPredictor(strategy_type="emoji")

    def get_prediction(self, text):
        return self.predictor.predict(text)