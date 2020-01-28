from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models.event import Event


class EventAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'start_date', 'start_time', 'publish_for_feed',
                    'is_tmp', 'end_date')
    raw_id_fields = ['creator', 'changed_by', 'parentusergroup']
    list_filter = ['start_date', 'publish_for_feed']
    search_fields = ['title']


admin.site.register(Event, EventAdmin)
