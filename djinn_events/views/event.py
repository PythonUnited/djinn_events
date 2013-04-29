from datetime import datetime
from djinn_contenttypes.views.base import DetailView


class EventView(DetailView):

    @property
    def has_start_time(self):

        return self.object.start_time

    @property
    def has_end_time(self):

        return self.object.end_time

    @property
    def has_end(self):

        return self.object.end_date

    @property
    def start(self):

        if self.has_start_time:
            return datetime.combine(self.object.start_date, 
                                    self.object.start_time)
        else:
            return self.object.start_date

    @property
    def end(self):

        if self.has_end_time:
            return datetime.combine(self.object.end_date, 
                                    self.object.end_time)
        else:
            return self.object.end_date
