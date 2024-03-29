from urllib.parse import unquote_plus
from django import forms
from django.conf import settings

from djinn_contenttypes.forms.crop import DjinnCroppingMixin
from djinn_contenttypes.models.feed import DESCR_FEED_MAX_LENGTH
from djinn_forms.fields.image import ImageField
from django.utils.translation import ugettext_lazy as _
from djinn_contenttypes.models import ImgAttachment
from djinn_forms.widgets.attachment import AttachmentWidget
from djinn_forms.widgets.image import ImageWidget
from djinn_forms.widgets.link import LinkWidget
from djinn_events.models.event import Event
from djinn_contenttypes.forms.base import BaseContentForm
from djinn_events import settings as events_settings


class EventForm(DjinnCroppingMixin, BaseContentForm):

    cropping_field_name = 'image_feed'

    # Translators: event edit general help
    help = _("Edit event")

    start_date = forms.DateField(
        label=_("Start date"),
        widget=forms.DateInput(
            attrs={'class': 'date', "placeholder": _("Date")},
            format=events_settings.DEFAULT_DATE_INPUT_FORMAT
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
            format=events_settings.DEFAULT_DATE_INPUT_FORMAT
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
        label=_("Add infoscreen image"),
        required=False,
        widget=ImageWidget(
            attrs={
                'size': 'upload_widget_feed',
                'attachment_type': 'djinn_contenttypes.ImgAttachment',
                }
        )
    )
    # Zo zou de widget gelijk zijn aan image toevoegen aan timelinebericht
    # image_feed = forms.ModelChoiceField(
    #     queryset=ImgAttachment.objects.all(),
    #     # Translators: Homepage rss-feed image label
    #     label=_("Add rss-feed image"),
    #     required=False,
    #     widget = AttachmentWidget(
    #         ImgAttachment,
    #         "gronet_v3/djinn_forms/snippets/imageattachmentwidget.html",
    #         attrs={"multiple": False, "show_progress": True,
    #                'inline_edit_enabled': settings.INLINE_EDIT_ENABLED}
    #     )
    # )

    def clean_link(self):

        """ Always store the unquoted version """

        return unquote_plus(self.cleaned_data['link'])

    def labels(self):

        return {'submit': _("Save event"),
                'cancel': _("Cancel"),
                'header': _("Add event")}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parentusergroup'].help_text = _(
            u"Voor vergeet-mij-nietjes op de homepage, kies 'Niet aan een groep "
            u"toevoegen'")
        self.fields['description_feed'].widget.attrs.update(
            {'data-maxchars': DESCR_FEED_MAX_LENGTH, 'class': 'full count_characters high'})


    class Meta(BaseContentForm.Meta):
        model = Event
        fields = [
            'start_date', 'start_time', 'end_date', 'end_time',
            'title', 'location', 'text', 'link', 'parentusergroup',
            'publish_for_feed', 'description_feed', 'use_default_image',
            'image_feed', 'image_feed_crop', 'userkeywords', 'owner'
        ]
