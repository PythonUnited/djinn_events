from pu_in_content.views.jsonbase import JSONCreateView, JSONDetailView, \
    JSONUpdateView, JSONDeleteView
from pgcontent.views.base import PGDetailView
from djinn_events.models.event import Event
from djinn_events.forms.event import EventForm


class EventCreateView(JSONCreateView):

    model = Event
    form_class = EventForm
    success_template_name = "djinn_events/snippets/event.html"

    def get_initial(self):

        return {'creator': self.request.user, 'changed_by': self.request.user}


class EventUpdateView(JSONUpdateView):

    model = Event
    form_class = EventForm
    success_template_name = "djinn_events/snippets/event.html"


class EventDeleteView(JSONDeleteView):

    model = Event


class EventDetailView(PGDetailView):

    model = Event

    def get_template_names(self):
        return ["djinn_events/snippets/event_detail.html"]
