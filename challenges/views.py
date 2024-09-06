from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Read a new book every week!",
    "april": "Practice mindfulness or meditation daily!",
    "may": "Learn a new skill or hobby!",
    "june": "Exercise for at least 30 minutes every day!",
    "july": "Reduce screen time to 1 hour per day!",
    "august": "Cook a new recipe every week!",
    "september": "Volunteer for a local charity or organization!",
    "october": "Spend at least 15 minutes outdoors every day!",
    "november": "Write in a journal every day!",
    "december": None,
}

def index(request):
   months = list(monthly_challenges.keys())
   return render(request, "challenges/index.html", {"months": months})

def monthly_challenge_by_number(request, month):
   try:
      months = list(monthly_challenges.keys())
      redirect_month = months[month]
      redirect_path = reverse("monthly_challenge", args=[redirect_month])
      return HttpResponseRedirect(redirect_path)
   except:
      return render(request, "404.html")

def monthly_challenge(request, month):
   challenge_text = None
   try:
      challenge_text=monthly_challenges[month]
      return render(request, "challenges/challenge.html", {"challenge_text": challenge_text, "month": month})
   except:
      return render(request, "404.html")