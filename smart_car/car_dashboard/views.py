from django.http import JsonResponse
from django.shortcuts import render
from .models import CarStatus

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

# Default values when no CarStatus record exists (e.g. fresh DB or demo/game mode)
DEFAULT_CAR_STATUS = {
    "speed": 0,
    "fuel": 60,
    "temperature": 20,
    "range": 320,
    "gear": "P",
    "song": "Mockingbird",
}


def car_status(request):
    data = CarStatus.objects.first()
    if data is None:
        return JsonResponse(DEFAULT_CAR_STATUS)
    response = {
        "speed": data.speed,
        "fuel": data.fuel,
        "temperature": data.temperature,
        "range": data.range_km,
        "gear": data.gear,
        "song": data.song,
    }
    return JsonResponse(response)


def dashboard_view(request):
    return render(request, "dashboard.html")
