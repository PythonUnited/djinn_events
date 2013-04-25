from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from pgcontent.registry import CTRegistry
from pgcontent.models.changeable import ChangeableBaseContent
from pgcontent.models.relatable import RelatableMixin


class Event(ChangeableBaseContent, RelatableMixin):

    title = models.CharField(_('Title'), max_length=200)
    text = models.TextField(_('Text'))
    start_date = models.DateField(_('Start date'))
    start_time = models.TimeField(_('Start time'))
    end_date = models.DateField(_('End date'), null=True,
                                blank=True, default=None)
    end_time = models.TimeField(_('End time'))
    location = models.CharField(_('Location'), max_length=50)
    link = models.URLField(_('Link'))

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
                     "user_can_add": True,
                     "app": "djinn_events",
                     "name": _("Event"),
                     "label": _("Event"),
                     "add_permission": "djinn_event.add_event",
                     "group_add": True,
                     "filter_label": "",
                     "name_plural": _("events")})
