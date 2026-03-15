from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm


# ---------------- HOME PAGE ---------------- #

def index(request):
    return render(request, 'index.html')


# ---------------- ADMIN LOGIN PAGE ---------------- #

def AdminLogin(request):
    return render(request, 'AdminLogin.html')


# ---------------- USER LOGIN PAGE ---------------- #

def UserLogin(request):
    return render(request, 'UserLogin.html')


# ---------------- USER REGISTRATION ---------------- #

def UserRegister(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            # Redirect to login page after registration
            return redirect('UserLogin')

    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'UserRegistrations.html', context)
