from datetime import date
from django.views.generic import TemplateView

from djinn_contenttypes.views.base import FeedViewMixin
from djinn_events.models.event import Event
from djinn_events.settings import SHOW_N_EVENTS
from pgprofile.models import GroupProfile


class EventViewlet(FeedViewMixin, TemplateView):

    template_name = "djinn_events/snippets/events_viewlet.html"

    def render_to_response(self, context, **response_kwargs):
        
        return super(EventViewlet, self).render_to_response(
            context,
            content_type='text/plain',
            **response_kwargs)

    def parentusergroup(self):

        return self.kwargs.get('parentusergroup', None)

    def groupprofile(self):

        pugid = self.parentusergroup()
        if pugid:
            return GroupProfile.objects.filter(usergroup__id=pugid).last()
        return None

    def get_context_data(self, **kwargs):

        ctx = super(EventViewlet, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx

    def events(self, limit=5):

        today = date.today()

        pug = self.parentusergroup()
        event_qs = self.get_queryset(Event.objects.filter(
            parentusergroup_id=pug))

        if self.kwargs.get('items_with_image', False):
            event_qs = event_qs.filter(image_feed__isnull=False)
        if self.kwargs.get('items_no_image', False):
            event_qs = event_qs.filter(image_feed__isnull=True)

        end_date_later_than_now = event_qs.filter(end_date__gte=today)
        no_end_date = event_qs.filter(end_date__isnull=True,
                                      start_date__gte=today)

        return (end_date_later_than_now | no_end_date).order_by(
            "start_date")[:limit]

    @property
    def show_more(self, limit=SHOW_N_EVENTS):

        return self.events(limit=None).count() > limit
