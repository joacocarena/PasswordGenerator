from django.shortcuts import render
import random

def homeFunc(request):
    return render(request, 'home.html')

def password(request):
    charactersList = list('abcdefghijklmnopqrstuvwxyz')
    
    generatedPass = ''
    passLength = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        charactersList.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('specialChar'):
        charactersList.extend(list('!@#$%^&*()-_+.:;<>?[]'))
    
    if request.GET.get('numbersOk'):
        charactersList.extend(list('0123456789'))
    
    for x in range(passLength):
        generatedPass += random.choice(charactersList)

    return render(request, 'password.html', {'password': generatedPass})