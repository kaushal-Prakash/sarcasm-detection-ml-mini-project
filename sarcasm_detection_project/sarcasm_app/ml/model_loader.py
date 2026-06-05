import pickle
import os

class ModelLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super(ModelLoader, cls).__new__(cls)

            base_path = os.path.dirname(os.path.dirname(__file__))  # sarcasm_app/
            model_path = os.path.join(base_path, "model_files", "text_model.pkl")
            vectorizer_path = os.path.join(base_path, "model_files", "vectorizer.pkl")

            with open(model_path, "rb") as f:
                instance.model = pickle.load(f)

            with open(vectorizer_path, "rb") as f:
                instance.vectorizer = pickle.load(f)

            cls._instance = instance

        return cls._instance