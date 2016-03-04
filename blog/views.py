from django.shortcuts import render, render_to_response
from datetime import datetime
from blog.models import Review
from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from random import randint

def hello(request):
    return render(request, "hello.html", { })


def hello_name(request, yourname):
    return render(request, "hello_name.html", { "yourname": yourname })


def imsleepy(request):
    return render(request, "imsleepy.html", {})

def time(request):
    return render(request, "time.html", {"timeNow": datetime.now()})

def all_reviews(request):
    return render(request, "all_reviews.html", {"revs": Review.objects.all()})

def no(request):
    return render(request, "no.html", {})

def new_review(request):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, "new_review.html", {"form":form})
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            review = form.cleaned_data['review']
            name = form.cleaned_data['name']
            new = Review(title=title, review=review, name=name, createdDate=datetime.now())
            new.save()
            return HttpResponseRedirect(reverse('all_reviews'))
        else:
            return render(request, "new_review.html", {"form":form})

class ReviewForm(forms.Form):
    title = forms.CharField(label="What game?", max_length=100)
    review = forms.CharField(label="What's your review?", max_length=500)
    name = forms.CharField(label="Your name", max_length=255)

def random(request):
    return render(request, "random.html",{"random": Review.objects.order_by('?')[0]})