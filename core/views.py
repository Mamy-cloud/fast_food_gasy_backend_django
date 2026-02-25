from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from core.services import mon_traitement

def cron_trigger(request):
    """
    Endpoint que UptimeRobot va appeler toutes les 10 min
    """
    try:
        data = mon_traitement()
        return JsonResponse({"status": "ok", "data": data})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)