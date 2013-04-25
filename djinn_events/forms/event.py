from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_events.models.event import Event


class EventForm(forms.ModelForm):

    start_date = forms.DateField(label=_("Start date"),
                                 widget=forms.DateTimeInput(
            attrs={'class': 'date'},
            format="%d-%m-%Y"
            )
                                 )
    
    start_time = forms.TimeField(label=_("Start time"),
                                 required=False,
                                 widget=forms.DateTimeInput(
            attrs={'class': 'time', 'size': 5},
            format="%H:%M"
            )
                                     )

    end_date = forms.DateField(label=_("End date"),
                               required=False,
                               widget=forms.DateInput(
            attrs={'class': 'date'},
            format="%d-%m-%Y"
            )
                               )

    end_time = forms.TimeField(label=_("End time"),
                               required=False,
                               widget=forms.DateTimeInput(
            attrs={'class': 'time', 'cols': 5},
            format="%H:%M"
            )
                                     )


    title = forms.CharField(label=_("Title"),
                            max_length=255)

    text = forms.CharField(label=_("Description"),
                           max_length=150,
                           widget=forms.Textarea(
                attrs={'data-maxchars': 150, 'rows': '3'})
                           )

    def labels(self):

        return {'submit': 'Plaats event', 
                'cancel': 'Annuleren',
                'header': 'Voeg event toe'}

    class Meta:
        widgets = {'creator': forms.HiddenInput(),
                   'changed_by': forms.HiddenInput()}
        model = Event
        fields = ('title', 'text', 'creator', 'changed_by', 'start_date',
                  'start_time',
                  'end_date', 'end_time', 'location', 'link')
