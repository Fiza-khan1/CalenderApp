from django.contrib import admin
from .models import Events

@admin.register(Events)
class EventsClass(admin.ModelAdmin):
    list_display=['person','day','start_date','end_date','notes']