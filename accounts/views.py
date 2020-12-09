from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.models import UserProfile


def user_profile(request, pk= None):
    pass


# class SignUpForm(UserCreationForm):

def signup_user(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm(),
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(request, user)
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def signout_user(request):
    logout(request)
    return redirect('index')