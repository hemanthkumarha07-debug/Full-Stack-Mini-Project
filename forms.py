from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CandidateUser, Event

class CandidateRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CandidateUser
        fields = ('username', 'email', 'password1', 'password2')

class CandidateLoginForm(AuthenticationForm):
    pass

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'image']
