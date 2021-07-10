from django.shortcuts import render

# Create your views here.
def HomeView(request):
    context = {
        "password": "aiugfjseuihuiiay",
        "username": "ghina"
    }
    return render(request, 'home.html', context)

def PasswordView(request):
    context = {}
    return render(request, 'password.html',context)