from django.contrib import admin
from cal_app.models import Event

# Register your models here.
admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('owner', 'title', 'description', 'start_time', 'end_time')
    