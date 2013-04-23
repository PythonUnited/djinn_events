from django.conf.urls.defaults import patterns, url, include
from views.event import EventCreateView, EventDetailView, EventDeleteView, \
    EventUpdateView
from views.eventviewlet import EventViewlet


_urlpatterns = patterns(
    "",

    # Events
    url(r"^event/(?P<pk>[\d]+)/?$",
        EventDetailView.as_view(),
        name="djinn_events_view_event"),

    url(r"^add/event/?$",
        EventCreateView.as_view(),
        name="djinn_events_add_event_json"),

    url(r"^edit/eventupdate/(?P<pk>[\d]+)/?$",
        EventUpdateView.as_view(),
        name="djinn_events_edit_event_json"),

    url(r"^delete/eventupdate/(?P<pk>[\d]+)/?$",
        EventDeleteView.as_view(),
        name="djinn_events_delete_event_json"),

    # Viewlet
    url(r"^$",
        EventViewlet.as_view(),
        name="djinn_events"),
    )

urlpatterns = patterns('',
    (r'^events/', include(_urlpatterns)),
)
