from django.urls import path
from . import views


app_name = 'appointments'
urlpatterns = [
    path('timeslot/create/', views.create_timeslot, name='create_timeslot'),
    path('timeslot/available/', views.available_timeslots, name='available_timeslots'),
    path('appointment/book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('appointment/<int:appointment_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),

]
