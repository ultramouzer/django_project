from django.shortcuts import render, render_to_response
from datetime import datetime

def hello(request):
    return render(request, "hello.html", { })


def hello_name(request, yourname):
    return render(request, "hello_name.html", { "yourname": yourname })


