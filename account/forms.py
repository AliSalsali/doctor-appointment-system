from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, PatientProfile


class PatientSignUpForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    phone_number = forms.CharField(max_length=20)
    national_id = forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_doctor = False
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user,
                age=self.cleaned_data.get('age'),
                phone_number=self.cleaned_data.get('phone_number'),
                national_id=self.cleaned_data.get('national_id')
            )
        return user



