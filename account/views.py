from django.shortcuts import render, redirect
from .forms import PatientSignUpForm
from django.contrib.auth import login ,logout
from django.contrib.auth.forms import AuthenticationForm


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('appointments:available_timeslots')
    else:
        form = PatientSignUpForm()
    return render(request, 'account/patient_signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('appointments:my_appointments')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('account:login')
