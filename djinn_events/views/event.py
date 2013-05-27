from djinn_contenttypes.views.base import DetailView
from djinn_contenttypes.utils import urn_to_object
from djinn_events.models import Event


class EventView(DetailView):

    model = Event

    @property
    def link(self):

        _link = (self.object.link or "").split("::")[0]
        
        if _link.startswith("urn"):
            return urn_to_object(_.link).get_absolute_url()
        else:
            return _link

    @property
    def link_target(self):

        return (self.object.link or "").split("::")[1]

    @property
    def link_title(self):

        _link = (self.object.link or "").split("::")[0]

        if _link.startswith("urn"):
            return urn_to_object(self.object.link).title
        else:
            return _link
