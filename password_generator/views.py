from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'password_generator/home.html')

def test(request):

    characters = list('asdfghjklqwertyuiopzxcvbnm')
    length = int(request.GET.get('length'))
    thepassword  = ''

    if request.GET.get('Uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('Symbols'):
        characters.extend(list(')(*&^%$#@!'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        thepassword +=random.choice(characters)

    return render(request, 'password_generator/test.html', {'password' :thepassword })

def creator(request):
    return render(request, 'password_generator/creator.html')