import json
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def load_data(path):
    texts = []
    labels = []

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            data = json.loads(line)
            texts.append(data['headline'])
            labels.append(data['is_sarcastic'])

    return texts, labels


def train():
    texts, labels = load_data("dataset/sarcasm_dataset.jsonl")

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    model = LogisticRegression(max_iter=1000)
    model.fit(X, labels)

    with open("sarcasm_app/model_files/text_model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("sarcasm_app/model_files/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Model trained and saved!")


if __name__ == "__main__":
    train()