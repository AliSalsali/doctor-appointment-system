from django.shortcuts import render, redirect
from .forms import PatientSignUpForm
from django.contrib.auth import login


def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'account/patient_signup.html', {'form': form})
