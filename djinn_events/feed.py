from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import feedgenerator
from django.utils.feedgenerator import Enclosure
from django.utils.safestring import mark_safe

from djinn_events.views.eventviewlet import EventViewlet
from djinn_news.views.newsviewlet import NewsViewlet
from pgcontent.templatetags.contentblock_tags import fetch_image_url
from pgprofile.models import GroupProfile


class LatestEventsFeed(Feed):
    '''
    http://192.168.1.6:8000/news/latest/feed/
    '''
    title_prefix = "Gronet:"
    title = "%s laatste vergeet-me-nietjes" % title_prefix
    link = "/events/latest/feed/"
    description = "Homepage laatste vergeet-me-nietjes"
    feed_type = feedgenerator.DefaultFeed

    def items(self):
        # re-use the news viewlet as it is on the homepage.
        eventviewlet = EventViewlet()
        eventviewlet.kwargs = {
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

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        # TODO: nadenken over detail pagina die niet achter inlog zit?
        # return reverse('djinn_news_view_news', args=[
        #     item.content_object.pk, item.content_object.slug])
        return "/"
