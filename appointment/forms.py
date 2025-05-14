from django import forms
from .models import TimeSlot, Appointment


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['date', 'start_time', 'end_time']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['reason']
