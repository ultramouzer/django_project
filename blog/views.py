from django.shortcuts import render, render_to_response
from datetime import datetime

def hello(request):
    return render(request, "hello.html", { "current_time": str(datetime.now()) })


def aboutme(request, yourname):
    return render(request, "aboutme.html", { "yourname": yourname })


