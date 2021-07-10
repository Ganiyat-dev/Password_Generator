from django.shortcuts import render
import random

# Create your views here.
def HomeView(request):
    return render(request, 'home.html')

def PasswordView(request):
    charaters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    
    length = request.GET.get('length')
    password = ''

    for i in range(int(length)):
        password += random.choice(charaters)

    
    context = {'password': password}
    return render(request, 'password.html', context)