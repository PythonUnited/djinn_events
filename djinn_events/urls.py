from django.conf.urls import url
from django.urls import include, path

from djinn_events.feed import LatestEventsFeed
from .views.eventviewlet import EventViewlet
from .models.event import Event
from djinn_contenttypes.views.utils import generate_model_urls


_urlpatterns = [

    # Viewlet
    url(r"^$",
        EventViewlet.as_view(),
        name="djinn_events"),

    # homepage nieuws-feed voor narrowcasting
    path('latest/feed/', LatestEventsFeed()),

]


urlpatterns = [
    url(r'^events/', include(_urlpatterns)),
    url(r'^events/', include(generate_model_urls(Event))),
]
