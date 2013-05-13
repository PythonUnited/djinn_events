from django.conf.urls.defaults import patterns, url, include
from views.eventviewlet import EventViewlet
from models.event import Event
from forms.event import EventForm
from views.event import EventView
from djinn_contenttypes.views.utils import generate_model_urls


_urlpatterns = patterns(
    "",

    # Viewlet
    url(r"^$",
        EventViewlet.as_view(),
        name="djinn_events"),
    )

_eventpatterns = generate_model_urls(Event)

urlpatterns = patterns('',
    (r'^events/', include(_urlpatterns)),
    (r'^events/', include(_eventpatterns)),
)
