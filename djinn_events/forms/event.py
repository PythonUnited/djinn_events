from urllib import unquote_plus
from django import forms
from django.utils.translation import ugettext_lazy as _
from djinn_forms.widgets.link import LinkWidget
from djinn_events.models.event import Event
from djinn_contenttypes.forms.base import BaseContentForm


class EventForm(BaseContentForm):

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
                            max_length=50)

    location = forms.CharField(label=_("Location"),
                               max_length=50)

    text = forms.CharField(label=_("Description"),
                           max_length=500,
                           widget=forms.Textarea(
                attrs={'data-maxchars': 150, 'rows': '3'})
                           )

    link = forms.CharField(label=_("Link"),
                           max_length=200,
                           widget=LinkWidget())

    def clean_link(self):
        
        """ Always store the unquoted version """
        
        return unquote_plus(self.cleaned_data['link'])

    def labels(self):

        return {'submit': _("Save event"), 
                'cancel': _("Cancel"),
                'header': _("Add event")}

    class Meta:
        model = Event
        xxfields = ('title', 'text', 'start_date',
                  'start_time',
                  'end_date', 'end_time', 'location', 'link')
