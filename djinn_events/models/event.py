from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from djinn_contenttypes.registry import CTRegistry
from djinn_contenttypes.models.base import BaseContent


class Event(BaseContent):

    text = models.TextField(_('Text'))
    start_date = models.DateField(_('Start date'))
    start_time = models.TimeField(_('Start time'), null=True, blank=True)
    end_date = models.DateField(_('End date'), null=True,
                                blank=True, default=None)
    end_time = models.TimeField(_('End time'), null=True, blank=True)
    location = models.CharField(_('Location'), max_length=200)
    link = models.CharField(_('Link'), max_length=200)

    @property
    def slug(self):
        
        return slugify(self.title)

    def __unicode__(self):

        return self.title

    @property
    def title_slice(self):

        """ Give title summary up to 50 chars """

        if len(self.title) > 50:
            return "%s..." % self.title[:50]
        return self.title

    class Meta:
        app_label = 'djinn_events'
        ordering = ('-created', )


CTRegistry.register("event", 
                    {"class": Event,
                     "app": "djinn_events",
                     "label": _("Event"),
                     "add_permission": "djinn_event.add_event",
                     "filter_label": "",
                     "name_plural": _("events")})
