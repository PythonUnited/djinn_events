from django.utils.safestring import mark_safe
from image_cropping.utils import get_backend
from pgprofile.models.groupprofile import GroupProfile

from djinn_contenttypes.base_feed import DjinnFeed
from djinn_contenttypes.models.feed import MoreInfoFeedGenerator
from djinn_contenttypes.settings import FEED_HEADER_HIGH_SIZE
from djinn_events.views.eventviewlet import EventViewlet


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
    title_prefix = "Gronet:"
    title = "%s laatste vergeet-me-nietjes" % title_prefix
    link = "/events/latest/feed/"
    description = "Homepage laatste vergeet-me-nietjes"
    feed_type = EventFeedGenerator

    parentusergroup_id = None

    def get_object(self, request, *args, **kwargs):

        groupprofile_id = kwargs.get('groupprofile_id', None)

        if groupprofile_id:
            groupprofile = GroupProfile.objects.get(id=groupprofile_id)
            self.title = "%s nieuws van '%s'" % (
                self.title_prefix, groupprofile.title)
            self.description = "%s laatste nieuwsartikelen in %s" % (
                self.title_prefix, groupprofile.title)
            self.parentusergroup_id = groupprofile.usergroup_id

        return super().get_object(request, *args, **kwargs)

    def items(self):
        # re-use the news viewlet as it is on the homepage.
        eventviewlet = EventViewlet()
        eventviewlet.kwargs = {
            'parentusergroup': self.parentusergroup_id,
            'for_rssfeed': True
        }

        eventlist = eventviewlet.events()
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

        return {
            "background_img_url": "%s%s" % (self.http_host, item.feed_bg_img_url),
            "more_info_class": item.more_info_class,
            "more_info_text": item.more_info_text,
            "more_info_qrcode_url": item.qrcode_img_url() or '',
            "event_start_date": str(item.start_date or ''),
            "event_start_time": str(item.start_time or ''),
            "event_end_date": str(item.end_date or ''),
            "event_end_time": str(item.end_time or ''),
            "event_location": item.location or ''
        }