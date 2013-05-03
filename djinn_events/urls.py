from django.conf.urls.defaults import patterns, url, include
from views.eventviewlet import EventViewlet
from models.event import Event
from forms.event import EventForm
from views.event import EventView
from djinn_contenttypes.views.base import CreateView, UpdateView, DeleteView


_urlpatterns = patterns(
    "",

    # Events
    url(r"^event/(?P<pk>[\d]+)/(?P<slug>[^\/]+)/?$",
        EventView.as_view(model=Event),
        name="djinn_events_view_event"),

    url(r"^add/event/?$",
        CreateView.as_view(model=Event, form_class=EventForm),
        name="djinn_events_add_event"),

    url(r"^edit/event/(?P<pk>[\d]+)/?$",
        UpdateView.as_view(model=Event, form_class=EventForm),
        name="djinn_events_edit_event"),

    url(r"^delete/event/(?P<pk>[\d]+)/?$",
        DeleteView.as_view(model=Event),
        name="djinn_events_delete_event"),

    # Viewlet
    url(r"^$",
        EventViewlet.as_view(),
        name="djinn_events"),
    )

urlpatterns = patterns('',
    (r'^events/', include(_urlpatterns)),
)
