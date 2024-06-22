from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallary.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use renamed login function
            return redirect('subadmin')  # Redirect to the home page after successful login
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def auth_logout(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('login')