from django.core.management.base import BaseCommand
from appointment.models import Appointment
from django.utils import timezone
from datetime import timedelta
from appointment.utils import send_appointment_reminder


# python manage.py send_reminders
class Command(BaseCommand):
    help = 'Send email reminders for upcoming appointments'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        tomorrow = now.date() + timedelta(days=1)

        upcoming = Appointment.objects.filter(
            time_slot__date=tomorrow
        )
        for appointment in upcoming:
            send_appointment_reminder(appointment)
            self.stdout.write(self.style.SUCCESS(f"Reminder sent to {appointment.patient.email}"))
        if not upcoming:
            self.stdout.write("No upcoming appointments for tomorrow.")

