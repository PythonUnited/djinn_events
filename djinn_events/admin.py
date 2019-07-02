from django.contrib import admin
from .models.event import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', )
    raw_id_fields = ['creator', 'changed_by', 'parentusergroup']
    search_fields = ['title']


admin.site.register(Event, EventAdmin)
