from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
