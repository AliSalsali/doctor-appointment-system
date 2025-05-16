from django.core.mail import send_mail


def send_appointment_reminder(appointment):
    subject = 'Appointment Reminder'
    message = f"""
Dear {appointment.patient.first_name},

This is a reminder for your appointment with Dr. {appointment.time_slot.doctor.last_name} on {appointment.time_slot.date} at {appointment.time_slot.start_time}.

If you need to cancel, please visit the clinic site.

Thanks,
Clinic Team
"""
    recipient = appointment.patient.email
    send_mail(subject, message, 'clinic@example.com', [recipient])
