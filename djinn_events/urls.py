from django.conf.urls import url
from django.urls import include, path

from djinn_events.feed import LatestEventsFeed
from .views.eventviewlet import EventViewlet
from .models.event import Event
from djinn_contenttypes.views.base import CreateView
from djinn_contenttypes.views.utils import generate_model_urls, find_form_class


event_form = find_form_class(Event, "djinn_events")

_urlpatterns = [

    # Viewlet
    url(r"^$",
        EventViewlet.as_view(),
        name="djinn_events"),

    url(r"^(?P<parentusergroup>[\d]*)/?$",
        EventViewlet.as_view(),
        name="djinn_events_pug"),

    url(r"^add/events/(?P<parentusergroup>[\d]*)/$",
        CreateView.as_view(model=Event, form_class=event_form,
                           fk_fields=["parentusergroup"]),
        name="djinn_events_add_event"),

    # homepage nieuws-feed voor narrowcasting
    path('latest/feed/', LatestEventsFeed()),

    # groepspagina events-feed voor narrowcasting
    # het groupprofile_id kan gevonden worden door in een groepspagina
    # boven de link naar 'Bekijk de content in deze groep' te bekijken
    path('latest/feed/group/<int:groupprofile_id>/', LatestEventsFeed()),

]


urlpatterns = [
    url(r'^events/', include(_urlpatterns)),
    url(r'^events/', include(generate_model_urls(Event))),
]
