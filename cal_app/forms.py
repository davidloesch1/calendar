from django import forms
from django.forms import ModelForm, DateTimeInput, DateTimeField, DateInput
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from cal_app.models import Event
class SignUpForm(UserCreationForm):
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'first', 'last', 'email', 'password1', 'password2')



class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format=('%Y-%m-%dT%H:%M')),
        }

        fields = ('title', 'description', 'start_time', 'end_time')

    def __init__(self, *args, **kargs):
        super(EventForm, self).__init__(*args, **kargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
