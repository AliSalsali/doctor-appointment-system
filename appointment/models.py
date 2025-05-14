from django.db import models
from django.conf import settings


class TimeSlot(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_doctor': True}
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_reserved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'start_time']
        unique_together = ('doctor', 'date', 'start_time')  # prevent duplicate times

    def __str__(self):
        return f"{self.date} | {self.start_time}-{self.end_time} | {self.doctor.username}"


class Appointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_patient': True}
    )
    time_slot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} -> {self.time_slot}"
