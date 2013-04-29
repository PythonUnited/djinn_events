from haystack import site
from djinn_events.models.event import Event
from pgsearch.base import ContentRealTimeSearchIndex


TPL = """%(title)s %(text)s"""


class EventIndex(ContentRealTimeSearchIndex):

    """ Index for events """

    def __init__(self, model, backend=None):

        super(EventIndex, self).__init__(model, backend=backend)

        self.fields['text'].template_name = \
            self.fields['content_auto'].template_name = \
            "indexes/event_index.txt"


site.register(Event, EventIndex)
