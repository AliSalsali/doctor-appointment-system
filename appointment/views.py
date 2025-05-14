from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TimeSlot, Appointment
from .forms import TimeSlotForm, AppointmentForm
from django.utils import timezone


# doctor adds new available times
@login_required
def create_timeslot(request):
    # if not request.user.is_doctor:
    #     return redirect('home')
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            timeslot = form.save(commit=False)
            timeslot.doctor = request.user
            timeslot.save()
            return redirect('doctor_timeslots')
    else:
        form = TimeSlotForm()
    return render(request, 'appointment/create_timeslot.html', {'form': form})


# patient sees available time slots
@login_required
def available_timeslots(request):
    slots = TimeSlot.objects.filter(is_reserved=False, date__gte=timezone.now().date())
    return render(request, 'appointment/available_timeslots.html', {'slots': slots})


# patient books a timeslot
@login_required
def book_appointment(request, slot_id):
    if not request.user.is_patient:
        return redirect('home')
    slot = get_object_or_404(TimeSlot, id=slot_id, is_reserved=False)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.time_slot = slot
            appointment.save()
            slot.is_reserved = True
            slot.save()
            return redirect('patient_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/book_appointment.html', {'form': form, 'slot': slot})
