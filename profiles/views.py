from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def view_profile(request):
    return render(request, 'view_profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')