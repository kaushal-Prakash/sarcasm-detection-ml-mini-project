def postprocess_prediction(prediction, proba, text):
    """
    Postprocess model predictions:
    1. Extract maximum probability as confidence.
    2. Apply rule-based boost for sarcastic emojis.
    3. Format final prediction result and confidence score.
    """
    confidence = max(proba)

    # 🔥 Rule-based boost
    sarcastic_emojis = ["😒", "🙄", "😑"]
    if any(e in text for e in sarcastic_emojis):
        prediction = 1
        confidence = max(confidence, 0.75)  # boost confidence

    result = "Sarcastic" if prediction == 1 else "Not Sarcastic"

    return {
        "result": result,
        "confidence": float(round(confidence * 100, 2))
    }
