from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")


def password(request):
    the_password = ''

    length = int(request.GET.get('length', 14))

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("uppercase"):
        characters.extend([x.upper() for x in characters])

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()[];:></?\\|'))

    if request.GET.get("number"):
        characters.extend(list('1234567890'))

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, "generator/password.html", {'password': the_password})


def about(request):
  return render(request, "generator/about.html")