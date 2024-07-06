from django.shortcuts import render
from django.http import HttpResponse
from .socket_client import send_data


def home(request):
    return render(request, "home.html")


def add(request):
    if request.method == "POST":
        data = request.POST["data"]
        if data:
            try:
                send_data(data)
                return HttpResponse("Data sent successfully.", status=200)
            except Exception as e:
                return HttpResponse(f"Failed to send data: {str(e)}", status=500)
    return HttpResponse("Invalid request", status=400)
