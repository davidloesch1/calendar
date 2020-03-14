from django.forms import ModelForm, DateTimeInput, DateTimeField, DateInput
from django.contrib.admin import widgets                                       

from cal_app.models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format=('%Y-%m-%dT%H:%M')),
        }

        fields = '__all__'

    def __init__(self, *args, **kargs):
        super(EventForm, self).__init__(*args, **kargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
