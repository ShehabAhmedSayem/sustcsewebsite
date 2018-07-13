from django.contrib import admin

from .models import Notice, News, Event, HonorBoard


class NoticeAdmin(admin.ModelAdmin):
    fields = (
        ('program_name', 'year_semester'),
        'title',
        'details',
        'upload',
    )

    list_display = ('title', 'program_name', 'year_semester', 'date_published')
    list_filter = ['date_published', 'year_semester']
    search_fields = ['title']


class NewsAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'details',
        'image',
    )

    list_display = ('title', 'date_published')
    list_filter = ['date_published']
    search_fields = ['title']


class EventAdmin(admin.ModelAdmin):
    fields = (
        ('title', 'event_date'),
        'location',
        'details',
        'image',
    )

    list_display = ('title', 'event_date')
    list_filter = ['event_date']
    search_fields = ['title']


class HonorBoardAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'details',
        'image',
    )

    list_display = ('title',)
    search_fields = ['title']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(HonorBoard, HonorBoardAdmin)

