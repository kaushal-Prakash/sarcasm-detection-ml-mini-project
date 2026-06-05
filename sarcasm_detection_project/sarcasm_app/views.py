from django.shortcuts import render
from sarcasm_app.services.prediction_service import PredictionService


def home(request):
    return render(request, "index.html")


def result(request):
    if request.method == "POST":
        text = request.POST.get("text")

        service = PredictionService()
        result = service.get_prediction(text)

        return render(request, "result.html", {
            "text": text,
            "prediction": result["result"],
            "confidence": result["confidence"]
        })

    return render(request, "index.html")