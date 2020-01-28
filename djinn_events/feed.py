from django.utils.safestring import mark_safe
from pgprofile.models.groupprofile import GroupProfile
from djinn_contenttypes.base_feed import DjinnFeed
from djinn_contenttypes.models.feed import MoreInfoFeedGenerator
from djinn_events.views.eventviewlet import EventViewlet
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from django.utils import formats


class EventFeedGenerator(MoreInfoFeedGenerator):

    def get_more_info_fields(self):
        infofields = super().get_more_info_fields()

        return infofields + ['event_location', 'event_start_date',
                             'event_start_time', 'event_end_date',
                             'event_end_time']


class LatestEventsFeed(DjinnFeed):
    '''
    http://192.168.1.6:8000/news/latest/feed/
    '''
    title_prefix = _("Gronet:")
    title = _(f"{title_prefix} laatste vergeet-me-nietjes")
    link = "/events/latest/feed/"
    description = _("Homepage laatste vergeet-me-nietjes")
    feed_type = EventFeedGenerator

    parentusergroup_id = None

    def get_object(self, request, *args, **kwargs):

        groupprofile_id = kwargs.get('groupprofile_id', None)

        if groupprofile_id:
            groupprofile = GroupProfile.objects.get(id=groupprofile_id)
            self.title = _(f"{self.title_prefix} nieuws van '{groupprofile.title}'")
            self.description = _(f"{self.title_prefix} laatste nieuwsartikelen in {groupprofile.title}")
            self.parentusergroup_id = groupprofile.usergroup_id

        return super().get_object(request, *args, **kwargs)

    def items(self):
        # re-use the news viewlet as it is on the homepage.
        eventviewlet = EventViewlet()
        eventviewlet.kwargs = {
            'parentusergroup': self.parentusergroup_id,
            'for_rssfeed': True,
            'items_no_image': self.items_no_image,
            'items_with_image': self.items_with_image,
        }

        eventlist = eventviewlet.events(limit=6)
        return eventlist

    def item_title(self, item):

        return item.title

    def item_description(self, item):
        # img_url = fetch_image_url(None,
        #                           'event_feed_default', 'event')
        # # img_url = "http://192.168.1.6:8000%s" % img_url
        # img_url = "%s" % img_url
        # # print(img_url)
        # desc = '<img src="%s" />' % img_url

        desc = '<div>%s</div>' % item.description_feed

        return mark_safe(desc)

    def item_extra_kwargs(self, item):
        background_img_url = ""
        if item.has_feedimg:
            background_img_url = "%s%s" % (self.http_host, item.feed_bg_img_url)

        # '''
        # If start time and end time are empty, the event is a full day
        # '''
        # start_date_str = formats.date_format(item.start_date, format="j F Y", use_l10n=True)
        # start_time_str = gettext("De hele dag")
        # end_time_str = ''
        # end_date_str = ''
        # if item.start_time:
        #     start_time_str = item.start_time.strftime('%H:%M')
        # if item.end_time:
        #     end_time_str = item.end_time.strftime('%H:%M')
        #
        # if item.end_date:
        #     end_date_str = formats.date_format(item.end_date, format="j F Y", use_l10n=True)

        return {
            "background_img_url": background_img_url,
            "more_info_class": item.more_info_class,
            "more_info_text": item.more_info_text,
            "more_info_qrcode_url": item.qrcode_img_url(http_host=self.http_host) or '',
            "event_start_date": item.feed_start_date,
            "event_start_time": item.feed_start_time,
            "event_end_date": item.feed_end_date,
            "event_end_time": item.feed_end_time,
            "event_location": item.location or ''
        }