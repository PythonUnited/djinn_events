from datetime import datetime, date
from django.db import models
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageRatioField
from djinn_contenttypes.models import ImgAttachment
from djinn_contenttypes.models.feed import FeedMixin
from djinn_contenttypes.registry import CTRegistry
from djinn_contenttypes.models.base import BaseContent
from djinn_contenttypes.settings import FEED_HEADER_HIGH_SIZE


class Event(FeedMixin, BaseContent):

    # BEGIN required by FeedMixin
    feed_bg_img_fieldname = 'image_feed'
    feed_bg_img_crop_fieldname = 'image_feed_crop'
    # END required by FeedMixin

    text = models.TextField(_('Text'))
    start_date = models.DateField(_('Start date'))
    start_time = models.TimeField(_('Start time'), null=True, blank=True)
    end_date = models.DateField(_('End date'), null=True,
                                blank=True, default=None)
    end_time = models.TimeField(_('End time'), null=True, blank=True)
    location = models.CharField(_('Location'), max_length=200)
    link = models.CharField(_('Link'), max_length=200)

    image_feed = models.ForeignKey(
        ImgAttachment,
        related_name='event_image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Image for the rss-feed")
    )

    image_feed_crop = ImageRatioField(
        'image_feed__image',
        "%sx%s" % (FEED_HEADER_HIGH_SIZE[0], FEED_HEADER_HIGH_SIZE[1]),
        help_text=_("Part of the image to use in the rss-feed"),
        verbose_name=_("Foto uitsnede")
    )

    @property
    def get_qrcode_target_url(self):
        return self.link

    @property
    def is_published(self):

        return super(Event, self).is_published and \
            (not self.end_date or (self.end_date < date.today()))

    @property
    def has_end(self):

        return self.end_time or \
            (self.end_date and self.end_date != self.start_date)

    @property
    def start(self):

        if self.start_time:
            return datetime.combine(self.start_date,
                                    self.start_time)
        else:
            return self.start_date

    @property
    def end(self):

        if self.end_time:
            return datetime.combine(self.end_date,
                                    self.end_time)
        else:
            return self.end_date

    class Meta:
        app_label = 'djinn_events'
        ordering = ('-start_date', )


CTRegistry.register("event",
                    {"class": Event,
                     "app": "djinn_events",
                     "label": _("Event"),
                     "global_add": True,
                     "allow_saveandedit": True,
                     "add_permission": "djinn_events.add_event",
                     "filter_label": _("Event"),
                     "name_plural": _("events")})
