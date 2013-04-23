from django.views.generic import TemplateView
from djinn_events.models.event import Event
from djinn_events.settings import SHOW_N_EVENTS


class EventViewlet(TemplateView):

    template_name = "djinn_events/snippets/events_viewlet.html"

    def render_to_response(self, context, **response_kwargs):
        
        return super(EventViewlet, self).render_to_response(
            context,
            content_type='text/plain',
            **response_kwargs)

    def get_context_data(self, **kwargs):

        ctx = super(EventViewlet, self).get_context_data(**kwargs)

        ctx['view'] = self

        return ctx

    def events(self, limit=5):

        return Event.objects.all()[:limit]

    @property
    def show_more(self, limit=SHOW_N_EVENTS):

        return self.events(limit=None).count() > limit
