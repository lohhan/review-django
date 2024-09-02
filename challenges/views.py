from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Complete a personal project or goal you've been putting off!",
}

def index(request):
   months = list(monthly_challenges.keys())
   html_content = ""
   for month in months:
      redirect_path = reverse("monthly_challenge", args=[month])
      html_content += f"<li><a href={redirect_path}>{month}</a></li>"
   return HttpResponse(f"<ul>{html_content}</ul>")

def monthly_challenge_by_number(request, month):
   try:
      months = list(monthly_challenges.keys())
      redirect_month = months[month]
      redirect_path = reverse("monthly_challenge", args=[redirect_month])
      return HttpResponseRedirect(redirect_path)
   except:
      return HttpResponseNotFound("Month was not found!")

def monthly_challenge(request, month):
   challenge_text = None
   try:
      challenge_text=monthly_challenges[month]
      return HttpResponse(challenge_text)
   except:
      return HttpResponseNotFound("Month was not found")