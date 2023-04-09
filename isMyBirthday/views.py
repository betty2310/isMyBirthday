from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    now = datetime.now()
    return render(request, "birthday/index.html", {
        "date": str(now.day) + "/" + str(now.month) + "/" + str(now.year),
        "is_bird_day": now.day == 23 and now.month == 10,
    })


def hello(request):
    return HttpResponse("hello")
