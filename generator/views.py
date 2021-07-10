from django.shortcuts import render

# Create your views here.
def HomeView(request):
    context = {}
    return render(request, 'home.html', context)

def PasswordView(request):
    context = {
        "password": "aiugfjseuihuiiay",
        "username": "ghina"
    }
    return render(request, 'password.html',context)