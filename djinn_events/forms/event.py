from django import forms
from djinn_events.models.event import Event


class EventForm(forms.ModelForm):

    def labels(self):

        return {'submit': 'Plaats mededeling', 
                'cancel': 'Annuleren',
                'header': 'Voeg mededeling toe'}

    class Meta:
        widgets = {'creator': forms.HiddenInput(),
                   'changed_by': forms.HiddenInput()}
        model = Event
        fields = ('title', 'text', 'creator', 'changed_by')
