from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')