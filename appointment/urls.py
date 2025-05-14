from django.urls import path
from . import views

urlpatterns = [
    path('timeslot/create/', views.create_timeslot, name='create_timeslot'),
    path('timeslot/available/', views.available_timeslots, name='available_timeslots'),
    path('appointment/book/<int:slot_id>/', views.book_appointment, name='book_appointment'),
]
