from django.urls import path
from . import views

urlpatterns = [
    path('signup/patient/', views.patient_signup, name='patient_signup'),
]
