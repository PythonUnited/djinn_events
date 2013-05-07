from djinn_contenttypes.views.base import DetailView
from djinn_contenttypes.utils import urn_to_object


class EventView(DetailView):

    @property
    def link(self):

        if self.object.link and self.object.link.startswith("urn"):
            return urn_to_object(self.object.link ).get_absolute_url()
        else:
            return self.object.link

    @property
    def link_title(self):

        if self.object.link and self.object.link.startswith("urn"):
            return urn_to_object(self.object.link).title
        else:
            return self.object.link
