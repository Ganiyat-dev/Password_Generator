from django.shortcuts import render
import random

# Create your views here.
def HomeView(request):
    return render(request, 'home.html')


# create a logic to get response of uppercase, lowercase and or special characters in generating the password
def PasswordView(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    
    
    length = int(request.GET.get('length'))
    password = ''

    for i in range(length):
        password += random.choice(characters)

    
    context = {"password": password}
    return render(request, 'password.html', context)