from urllib.parse import unquote_plus
from django import forms
from djinn_contenttypes.forms.crop import DjinnCroppingMixin
from djinn_forms.fields.image import ImageField
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.models import ImgAttachment
from djinn_forms.forms.relate import RelateMixin
from djinn_forms.widgets.image import ImageWidget
from djinn_forms.widgets.link import LinkWidget
from djinn_events.models.event import Event
from djinn_contenttypes.forms.base import BaseContentForm
from djinn_events import settings


class EventForm(DjinnCroppingMixin, BaseContentForm, RelateMixin):

    cropping_field_name = 'image_feed'

    # Translators: event edit general help
    help = _("Edit event")

    start_date = forms.DateField(
        label=_("Start date"),
        widget=forms.DateInput(
            attrs={'class': 'date', "placeholder": _("Date")},
            format=settings.DEFAULT_DATE_INPUT_FORMAT
        ))

    start_time = forms.TimeField(
        label=_("Start time"),
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'time', 'size': 5, "placeholder": _("Time")},
        ))

    end_date = forms.DateField(
        label=_("End date"),
        required=False,
        widget=forms.DateInput(
            attrs={'class': 'date', "placeholder": _("Date")},
            format=settings.DEFAULT_DATE_INPUT_FORMAT
        ))

    end_time = forms.TimeField(
        label=_("End time"),
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'time', 'size': 5, "placeholder": _("Time")},
        ))

    title = forms.CharField(
        label=_("Title"),
        help_text=_("50 characters max"),
        max_length=50,
        widget=forms.TextInput(
            attrs={'data-maxchars': 50,
                   'class': "count_characters"}
        ))

    location = forms.CharField(
        label=_("Location"),
        help_text=_("50 characters max"),
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={'data-maxchars': 50,
                   'class': "count_characters"}
        ))

    text = forms.CharField(
        label=_("Description"),
        help_text=_("500 characters max"),
        max_length=500,
        widget=forms.Textarea(
            attrs={'data-maxchars': 500,
                   'class': "count_characters description_feed_src",
                   'rows': '3'}
        ))

    link = forms.CharField(
        label=_("Link"),
        required=False,
        max_length=200,
        widget=LinkWidget())

    image_feed = ImageField(
        model=ImgAttachment,
        # Translators: Homepage event image label
        label=_("Add homepage image"),
        required=False,
        widget=ImageWidget(
            attrs={
                'size': 'feed_full',
                'attachment_type': 'djinn_contenttypes.ImgAttachment',
                }
        )
    )

    def clean_link(self):

        """ Always store the unquoted version """

        return unquote_plus(self.cleaned_data['link'])

    def labels(self):

        return {'submit': _("Save event"),
                'cancel': _("Cancel"),
                'header': _("Add event")}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_relation_fields()


    class Meta(BaseContentForm.Meta):
        model = Event
        fields = [
            'start_date', 'start_time', 'end_date', 'end_time',
            'title', 'location', 'text', 'link', 'parentusergroup',
            'publish_for_feed', 'description_feed',
            'image_feed', 'image_feed_crop'
        ]
