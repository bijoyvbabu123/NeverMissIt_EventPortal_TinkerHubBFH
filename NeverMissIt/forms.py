from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms
from . import models

# the form used in the signup page. It is inheriting from the built in Model provided by django.
class SignUpForm(UserCreationForm):
    class Meta:
        model = User # using the model django provides. django.contrib.auth.models.User
        fields = ['username', 'email', 'password1', 'password2'] # choosing the fields to include in the form.

# this is to provide datepicking widget to some input fields in EventCreationForm.
class DatePicker(forms.DateInput):
    input_type = 'date'

# form for the event publishing process.
class EventCreationForm(forms.ModelForm):
    class Meta:
        model = models.EventDetails # creating the model EventDetails defined in models.py
        fields = ['title', 'description', 'eventdate', 'location', 'lastdatetoreg', 'maxparticipants'] # choosing fields to be included in the form
        widgets = {
            'eventdate':DatePicker(), # providing a datepicking widget to two of the fields in the form.
            'lastdatetoreg':DatePicker(),
        }